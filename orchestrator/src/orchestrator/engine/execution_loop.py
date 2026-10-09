import time
from typing import Optional
from ..domain.models import Project, Task
from ..domain.enums import ProjectState, TaskState
from ..domain.state_machine import TaskStateMachine, ProjectStateMachine
from .scheduler import TaskScheduler
from ..persistence.repository import DatabaseRepository
from ..adapters.base import AgentAdapter

class ExecutionLoop:
    def __init__(self, repo: DatabaseRepository, adapter: AgentAdapter):
        self.repo = repo
        self.adapter = adapter

    def run_project(self, project_id: str):
        project = self.repo.load_project(project_id)
        if not project:
            raise ValueError("Project not found")

        if project.state == ProjectState.READY:
            ProjectStateMachine.transition_project(project, ProjectState.EXECUTING)
            self.repo.save_project(project)

        while True:
            project = self.repo.load_project(project_id)
            if project.state in [ProjectState.COMPLETED, ProjectState.FAILED, ProjectState.CANCELLED]:
                break

            ready_tasks = TaskScheduler.get_ready_tasks(project)
            
            if not ready_tasks:
                if TaskScheduler.is_project_completed(project):
                    ProjectStateMachine.transition_project(project, ProjectState.FINAL_AUDIT)
                    ProjectStateMachine.transition_project(project, ProjectState.COMPLETED)
                    self.repo.save_project(project)
                    break
                else:
                    # Check for blocked tasks or running tasks
                    running = [t for t in project.tasks.values() if t.state == TaskState.RUNNING]
                    if not running:
                        # Deadlock
                        ProjectStateMachine.transition_project(project, ProjectState.FAILED)
                        self.repo.save_project(project)
                        break
                    time.sleep(1) # wait for running tasks
                    continue

            for task in ready_tasks:
                self._execute_task(project, task)
                
            self.repo.save_project(project)

    def _execute_task(self, project: Project, task: Task):
        if task.state == TaskState.PENDING:
            TaskStateMachine.transition_task(task, TaskState.READY)
        TaskStateMachine.transition_task(task, TaskState.ASSIGNED)
        TaskStateMachine.transition_task(task, TaskState.RUNNING)
        self.repo.save_project(project)

        try:
            result = self.adapter.dispatch_task(task, project.context)
            if result.get("status") == "PASS":
                task.output = result
                TaskStateMachine.transition_task(task, TaskState.SUCCEEDED)
            else:
                self._handle_failure(project, task, result.get("summary", "Unknown error"))
        except Exception as e:
            self._handle_failure(project, task, str(e))
            
    def _handle_failure(self, project: Project, task: Task, error: str):
        task.error = error
        task.retries += 1
        if task.retries >= task.max_retries:
            TaskStateMachine.transition_task(task, TaskState.FAILED)
        else:
            TaskStateMachine.transition_task(task, TaskState.REPAIR_REQUIRED)
            TaskStateMachine.transition_task(task, TaskState.READY)
        self.repo.save_project(project)

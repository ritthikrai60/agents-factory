from typing import List
from ..domain.models import Project, Task
from ..domain.enums import TaskState

class TaskScheduler:
    @staticmethod
    def get_ready_tasks(project: Project) -> List[Task]:
        ready_tasks = []
        for task in project.tasks.values():
            if task.state in [TaskState.PENDING, TaskState.READY]:
                # Check if dependencies are met
                dependencies_met = True
                for dep_id in task.dependencies:
                    dep_task = project.tasks.get(dep_id)
                    if not dep_task or dep_task.state != TaskState.SUCCEEDED:
                        dependencies_met = False
                        break
                
                if dependencies_met:
                    ready_tasks.append(task)
                    
        return ready_tasks

    @staticmethod
    def is_project_completed(project: Project) -> bool:
        if not project.tasks:
            return False
        return all(task.state == TaskState.SUCCEEDED for task in project.tasks.values())

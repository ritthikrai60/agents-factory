from .enums import ProjectState, TaskState
from .models import Project, Task

class ProjectStateMachine:
    @staticmethod
    def can_transition(current: ProjectState, target: ProjectState) -> bool:
        # A simplified transition logic for prototype
        transitions = {
            ProjectState.CREATED: [ProjectState.DISCOVERY, ProjectState.CANCELLED],
            ProjectState.DISCOVERY: [ProjectState.REQUIREMENTS, ProjectState.FAILED],
            ProjectState.REQUIREMENTS: [ProjectState.PLANNING, ProjectState.FAILED],
            ProjectState.PLANNING: [ProjectState.READY, ProjectState.FAILED],
            ProjectState.READY: [ProjectState.EXECUTING],
            ProjectState.EXECUTING: [ProjectState.INTEGRATING, ProjectState.FINAL_AUDIT, ProjectState.BLOCKED, ProjectState.FAILED],
            ProjectState.INTEGRATING: [ProjectState.VERIFYING, ProjectState.FAILED],
            ProjectState.VERIFYING: [ProjectState.REPAIRING, ProjectState.FINAL_AUDIT, ProjectState.FAILED],
            ProjectState.REPAIRING: [ProjectState.VERIFYING, ProjectState.FAILED, ProjectState.BLOCKED],
            ProjectState.FINAL_AUDIT: [ProjectState.COMPLETED, ProjectState.FAILED],
            ProjectState.BLOCKED: [ProjectState.EXECUTING, ProjectState.CANCELLED],
        }
        allowed = transitions.get(current, [])
        return target in allowed

    @staticmethod
    def transition_project(project: Project, target: ProjectState):
        if ProjectStateMachine.can_transition(project.state, target):
            project.state = target
        else:
            raise ValueError(f"Invalid transition from {project.state} to {target}")

class TaskStateMachine:
    @staticmethod
    def can_transition(current: TaskState, target: TaskState) -> bool:
        transitions = {
            TaskState.PENDING: [TaskState.READY, TaskState.CANCELLED],
            TaskState.READY: [TaskState.ASSIGNED, TaskState.CANCELLED],
            TaskState.ASSIGNED: [TaskState.RUNNING, TaskState.FAILED],
            TaskState.RUNNING: [TaskState.REVIEW_REQUIRED, TaskState.VERIFICATION_REQUIRED, TaskState.SUCCEEDED, TaskState.FAILED],
            TaskState.REVIEW_REQUIRED: [TaskState.VERIFICATION_REQUIRED, TaskState.REPAIR_REQUIRED],
            TaskState.VERIFICATION_REQUIRED: [TaskState.SUCCEEDED, TaskState.REPAIR_REQUIRED],
            TaskState.REPAIR_REQUIRED: [TaskState.READY, TaskState.BLOCKED, TaskState.FAILED],
            TaskState.FAILED: [TaskState.READY, TaskState.BLOCKED]
        }
        allowed = transitions.get(current, [])
        return target in allowed

    @staticmethod
    def transition_task(task: Task, target: TaskState):
        if TaskStateMachine.can_transition(task.state, target):
            task.state = target
        else:
            raise ValueError(f"Invalid transition from {task.state} to {target}")

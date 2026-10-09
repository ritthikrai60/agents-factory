from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from .enums import ProjectState, TaskState

class Task(BaseModel):
    id: str
    objective: str
    state: TaskState = TaskState.PENDING
    dependencies: List[str] = Field(default_factory=list)
    owner: Optional[str] = None
    retries: int = 0
    max_retries: int = 3
    output: Optional[Dict[str, Any]] = None
    evidence: Optional[str] = None
    error: Optional[str] = None

class Project(BaseModel):
    id: str
    name: str
    state: ProjectState = ProjectState.CREATED
    tasks: Dict[str, Task] = Field(default_factory=dict)
    context: Dict[str, Any] = Field(default_factory=dict)

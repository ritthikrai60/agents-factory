from abc import ABC, abstractmethod
from typing import Dict, Any
from ..domain.models import Task

class AgentAdapter(ABC):
    @abstractmethod
    def dispatch_task(self, task: Task, context: Dict[str, Any]) -> Dict[str, Any]:
        """Dispatches a task to the agent and returns a structured result."""
        pass

class MockAdapter(AgentAdapter):
    def dispatch_task(self, task: Task, context: Dict[str, Any]) -> Dict[str, Any]:
        """A mock implementation that simply simulates a successful agent run."""
        return {
            "status": "PASS",
            "summary": f"Simulated execution for {task.objective}",
            "changed_files": ["mock_file.txt"],
            "tests_executed": ["mock_test"],
            "test_results": "PASS"
        }

class AntigravityAdapter(AgentAdapter):
    def dispatch_task(self, task: Task, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Placeholder for real Antigravity SDK invocation.
        In reality, this would lease an agent via the SDK, pass the context,
        and wait for completion or async webhook.
        """
        raise NotImplementedError("Antigravity Python SDK integration requires actual SDK package")

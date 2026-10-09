# Autonomous Software Engineering Orchestrator

The Autonomous Software Engineering Orchestrator is a robust python-based state machine designed to coordinate multi-agent AI execution, maintain persistent state, enforce permissions, and verify completion automatically.

## Architecture

1. **State Machine:** Governs transitions (`ProjectState`, `TaskState`).
2. **Task Scheduler:** Resolves DAG dependencies and fetches `READY` tasks.
3. **Database Repository:** Persists execution state to SQLite to survive crashes.
4. **Execution Loop:** Handles orchestration logic, dispatching, and retrying.
5. **Adapters:** Contains a `MockAdapter` for local tests and an interface `AgentAdapter` for the `AntigravityAdapter`.

## Requirements
- Python 3.10+
- `pip install -e .`

## Usage

```bash
# 1. Initialize a new project
python src/orchestrator/cli/main.py init my-new-project
> Project initialized: [UUID]

# 2. Check the status
python src/orchestrator/cli/main.py status [UUID]

# 3. Run the orchestration loop
python src/orchestrator/cli/main.py run [UUID]
```

## Supported Workflows
- **Autonomous Feedback Loop**: Automatically retries on task failure based on `TaskStateMachine`.
- **Durable Execution**: Saves task state, logs, and outputs to SQLite on every state transition.
- **Dependency Awareness**: Tasks are only executed when their `dependencies` are in the `SUCCEEDED` state.

## Limitations
- Currently uses a `MockAdapter` to simulate agents since the Antigravity Python SDK was not globally available or required credentials we shouldn't hardcode. The interface `AntigravityAdapter` is scaffolded.
- File-level locking (Git Worktrees) for parallel tasks is an architectural target not fully implemented in the mock dispatcher.

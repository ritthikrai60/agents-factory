import click
from orchestrator.persistence.repository import DatabaseRepository
from orchestrator.domain.models import Project, Task
from orchestrator.engine.execution_loop import ExecutionLoop
from orchestrator.adapters.base import MockAdapter
import uuid

@click.group()
def cli():
    """Autonomous Software Engineering Orchestrator CLI"""
    pass

@cli.command()
@click.argument('name')
def init(name):
    """Initialize a new project"""
    repo = DatabaseRepository()
    project_id = str(uuid.uuid4())
    project = Project(id=project_id, name=name)
    from orchestrator.domain.enums import ProjectState
    project.state = ProjectState.READY
    
    # Add a couple of dummy tasks for demonstration
    t1 = Task(id=str(uuid.uuid4()), objective="Setup repo")
    t2 = Task(id=str(uuid.uuid4()), objective="Write tests", dependencies=[t1.id])
    
    project.tasks[t1.id] = t1
    project.tasks[t2.id] = t2
    
    repo.save_project(project)
    click.echo(f"Project initialized: {project_id}")

@cli.command()
@click.argument('project_id')
def run(project_id):
    """Run the orchestrator for a project"""
    repo = DatabaseRepository()
    adapter = MockAdapter()
    loop = ExecutionLoop(repo, adapter)
    click.echo(f"Starting execution for project {project_id}...")
    loop.run_project(project_id)
    
    project = repo.load_project(project_id)
    click.echo(f"Execution finished. Project state: {project.state.value}")
    
@cli.command()
@click.argument('project_id')
def status(project_id):
    """Check project status"""
    repo = DatabaseRepository()
    project = repo.load_project(project_id)
    if not project:
        click.echo("Project not found.")
        return
        
    click.echo(f"Project: {project.name} | State: {project.state.value}")
    for task in project.tasks.values():
        click.echo(f"  Task {task.id[:8]}... | {task.state.value} | {task.objective}")

if __name__ == '__main__':
    cli()

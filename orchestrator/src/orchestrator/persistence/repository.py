import sqlite3
from typing import Optional, List
from ..domain.models import Project, Task
import json

class DatabaseRepository:
    def __init__(self, db_path="orchestrator.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS projects (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    state TEXT,
                    context TEXT
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id TEXT PRIMARY KEY,
                    project_id TEXT,
                    objective TEXT,
                    state TEXT,
                    dependencies TEXT,
                    owner TEXT,
                    retries INTEGER,
                    output TEXT,
                    evidence TEXT,
                    error TEXT,
                    FOREIGN KEY(project_id) REFERENCES projects(id)
                )
            ''')

    def save_project(self, project: Project):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                INSERT OR REPLACE INTO projects (id, name, state, context)
                VALUES (?, ?, ?, ?)
            ''', (project.id, project.name, project.state.value, json.dumps(project.context)))
            
            for task in project.tasks.values():
                conn.execute('''
                    INSERT OR REPLACE INTO tasks 
                    (id, project_id, objective, state, dependencies, owner, retries, output, evidence, error)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    task.id, project.id, task.objective, task.state.value, 
                    json.dumps(task.dependencies), task.owner, task.retries, 
                    json.dumps(task.output) if task.output else None, task.evidence, task.error
                ))

    def load_project(self, project_id: str) -> Optional[Project]:
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute('SELECT id, name, state, context FROM projects WHERE id = ?', (project_id,)).fetchone()
            if not row:
                return None
            
            project = Project(
                id=row[0],
                name=row[1],
                state=row[2],
                context=json.loads(row[3])
            )

            task_rows = conn.execute('SELECT * FROM tasks WHERE project_id = ?', (project_id,)).fetchall()
            for r in task_rows:
                task = Task(
                    id=r[0],
                    objective=r[2],
                    state=r[3],
                    dependencies=json.loads(r[4]),
                    owner=r[5],
                    retries=r[6],
                    output=json.loads(r[7]) if r[7] else None,
                    evidence=r[8],
                    error=r[9]
                )
                project.tasks[task.id] = task
                
            return project

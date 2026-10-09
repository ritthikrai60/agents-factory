import yaml
import json
import os
from pydantic import BaseModel
from typing import Dict, Any

class OrchestratorConfig(BaseModel):
    max_concurrent_agents: int = 4
    max_repair_attempts: int = 3
    database_url: str = "sqlite:///orchestrator.db"

def load_config() -> OrchestratorConfig:
    return OrchestratorConfig()

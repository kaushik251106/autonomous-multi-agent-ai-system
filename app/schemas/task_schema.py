from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskRequest(BaseModel):
    task: str


class TaskResponse(BaseModel):
    task_id: str
    status: str
    task: str
    created_at: datetime
    result: Optional[str] = None
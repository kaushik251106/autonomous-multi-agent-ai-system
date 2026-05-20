from pydantic import BaseModel

from datetime import datetime

from typing import Optional
from typing import Dict
from typing import Any


class TaskRequest(BaseModel):

    task: str


class TaskResponse(BaseModel):

    task_id: str

    status: str

    task: str

    created_at: datetime

    workflow: Optional[Dict[str, Any]] = None

    result: Optional[Any] = None
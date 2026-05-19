import uuid
import asyncio

from datetime import datetime

from app.schemas.task_schema import (
    TaskRequest,
    TaskResponse
)


class TaskService:

    def __init__(self):

        self.tasks = {}

    async def process_task(
        self,
        task_data: TaskRequest
    ) -> TaskResponse:

        task_id = str(uuid.uuid4())

        task = TaskResponse(
            task_id=task_id,
            status="pending",
            task=task_data.task,
            created_at=datetime.utcnow(),
            result=None
        )

        self.tasks[task_id] = task

        asyncio.create_task(
            self.execute_task(task_id)
        )

        return task

    async def execute_task(
        self,
        task_id: str
    ):

        task = self.tasks[task_id]

        task.status = "running"

        await asyncio.sleep(5)

        task.status = "completed"

        task.result = (
            f"AI processed task: {task.task}"
        )

    async def get_task(
        self,
        task_id: str
    ):

        return self.tasks.get(task_id)


task_service = TaskService()
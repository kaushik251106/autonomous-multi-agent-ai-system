import uuid
import asyncio

from datetime import datetime

from app.schemas.task_schema import (
    TaskRequest,
    TaskResponse
)

from app.services.openai_service import (
    openai_service
)

from app.core.logging_config import (
    logger
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

        try:

            task = self.tasks[task_id]

            logger.info(
                f"Executing task: {task.task}"
            )

            task.status = "running"

            ai_result = await openai_service.generate_response(
                task.task
            )

            logger.info(
                f"OpenAI response received"
            )

            task.status = "completed"

            task.result = ai_result

        except Exception as e:

            logger.error(
                f"Task execution failed: {str(e)}"
            )

            task.status = "failed"

            task.result = str(e)

    async def get_task(
        self,
        task_id: str
    ):

        return self.tasks.get(task_id)


task_service = TaskService()
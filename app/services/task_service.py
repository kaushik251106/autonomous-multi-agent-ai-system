import uuid
import asyncio

from datetime import datetime

from app.schemas.task_schema import (
    TaskRequest,
    TaskResponse
)

from app.services.openrouter_service import (
    openrouter_service
)

from app.services.workflow_classifier import (
    workflow_classifier
)

from app.core.logging_config import (
    logger
)


class TaskService:

    def __init__(self):

        logger.info(
            "Initializing TaskService"
        )

        self.tasks = {}

    async def process_task(
        self,
        task_data: TaskRequest
    ) -> TaskResponse:

        task_id = str(uuid.uuid4())

        workflow = await workflow_classifier.classify_task(
            task_data.task
        )

        task = TaskResponse(

            task_id=task_id,

            status="pending",

            task=task_data.task,

            created_at=datetime.utcnow(),

            workflow=workflow.dict(),

            result=None
        )

        self.tasks[task_id] = task

        logger.info(
            f"Stored task: {task_id}"
        )

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

            task.status = "running"

            ai_result = await openrouter_service.generate_response(
                task.task
            )

            task.result = ai_result

            task.status = "completed"

            logger.info(
                f"Task completed: {task_id}"
            )

        except Exception as e:

            logger.error(
                f"Task execution failed: {str(e)}"
            )

            task.status = "failed"

            task.result = {

                "error": str(e)
            }

    async def get_task(
        self,
        task_id: str
    ):

        return self.tasks.get(task_id)


task_service = TaskService()
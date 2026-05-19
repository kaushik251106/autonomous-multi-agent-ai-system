from fastapi import APIRouter

from app.schemas.task_schema import (
    TaskRequest
)

from app.schemas.base_schema import (
    APIResponse
)

from app.services.task_service import (
    task_service
)

from app.core.exceptions import (
    TaskNotFoundException
)

router = APIRouter(
    tags=["Tasks"]
)


@router.post(
    "/tasks",
    response_model=APIResponse
)
async def create_task(
    task_data: TaskRequest
):

    task = await task_service.process_task(
        task_data
    )

    return APIResponse(
        success=True,
        message="Task created successfully",
        data=task
    )


@router.get(
    "/tasks/{task_id}",
    response_model=APIResponse
)
async def get_task(
    task_id: str
):

    task = await task_service.get_task(
        task_id
    )

    if not task:

        raise TaskNotFoundException(
            task_id=task_id
        )

    return APIResponse(
        success=True,
        message="Task fetched successfully",
        data=task
    )
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

import time

from app.core.config import settings

from app.core.logging_config import (
    logger
)

from app.core.exceptions import (
    TaskNotFoundException
)

from app.api.routes.health import (
    router as health_router
)

from app.api.routes.tasks import (
    router as tasks_router
)

from app.api.routes.research import (
    router as research_router
)


app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0"
)


@app.on_event("startup")
async def startup_event():

    logger.info(
        "AI Agent System starting up..."
    )


@app.on_event("shutdown")
async def shutdown_event():

    logger.info(
        "AI Agent System shutting down..."
    )


@app.middleware("http")
async def log_requests(
    request: Request,
    call_next
):

    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    logger.info(
        f"{request.method} "
        f"{request.url.path} "
        f"completed in "
        f"{process_time:.4f} seconds"
    )

    return response


@app.exception_handler(
    TaskNotFoundException
)
async def task_not_found_handler(
    request: Request,
    exc: TaskNotFoundException
):

    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "message": (
                f"Task with ID "
                f"{exc.task_id} not found"
            )
        }
    )


app.include_router(
    health_router,
    prefix=settings.API_V1_STR
)

app.include_router(
    tasks_router,
    prefix=settings.API_V1_STR
)

app.include_router(
    research_router,
    prefix=settings.API_V1_STR
)


@app.get(
    "/",
    tags=["Root"]
)
async def root():

    logger.info(
        "Root endpoint accessed"
    )

    return {
        "message": (
            "Autonomous Multi-Agent "
            "AI System Running"
        )
    }
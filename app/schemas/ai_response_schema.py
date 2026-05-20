from pydantic import BaseModel


class AIResponseSchema(BaseModel):

    task_type: str

    summary: str

    confidence: float

    next_action: str
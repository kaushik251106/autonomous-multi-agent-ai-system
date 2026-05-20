from pydantic import BaseModel


class WorkflowClassification(BaseModel):

    workflow_type: str

    priority: str

    requires_memory: bool

    requires_research: bool
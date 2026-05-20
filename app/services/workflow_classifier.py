from app.schemas.workflow_schema import (
    WorkflowClassification
)


class WorkflowClassifier:

    async def classify_task(
        self,
        task: str
    ) -> WorkflowClassification:

        task_lower = task.lower()

        workflow_type = "general"

        priority = "medium"

        requires_memory = False

        requires_research = False

        if (
            "research" in task_lower
            or "analyze" in task_lower
        ):

            workflow_type = "research"

            requires_research = True

        elif (
            "code" in task_lower
            or "python" in task_lower
        ):

            workflow_type = "coding"

        elif (
            "memory" in task_lower
            or "remember" in task_lower
        ):

            workflow_type = "memory"

            requires_memory = True

        if (
            "urgent" in task_lower
            or "important" in task_lower
        ):

            priority = "high"

        return WorkflowClassification(

            workflow_type=workflow_type,

            priority=priority,

            requires_memory=requires_memory,

            requires_research=requires_research
        )


workflow_classifier = WorkflowClassifier()
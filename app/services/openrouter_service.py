import json

from openai import AsyncOpenAI

from app.core.config import settings

from app.core.logging_config import (
    logger
)

from app.prompts.prompt_manager import (
    prompt_manager
)


class OpenRouterService:

    def __init__(self):

        self.client = AsyncOpenAI(
            api_key=settings.OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1"
        )

    async def generate_response(
        self,
        prompt: str
    ):

        logger.info(
            "Sending request to OpenRouter"
        )

        try:

            messages = (
                prompt_manager.build_chat_messages(
                    prompt
                )
            )

            response = await self.client.chat.completions.create(

                model="openchat/openchat-7b:free",

                messages=messages,

                temperature=0.3
            )

            content = (
                response
                .choices[0]
                .message
                .content
            )

            logger.info(
                "Received OpenRouter response"
            )

            try:

                return json.loads(content)

            except Exception:

                return {

                    "task_type": "general",

                    "summary": content,

                    "confidence": 0.5,

                    "next_action": "manual_review"
                }

        except Exception as e:

            logger.error(
                f"Provider error: {str(e)}"
            )

            return {

                "task_type": "provider_error",

                "summary": str(e),

                "confidence": 0.0,

                "next_action": "retry"
            }


openrouter_service = OpenRouterService()
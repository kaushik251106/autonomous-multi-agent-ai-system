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
    ) -> str:

        logger.info(
            "Sending request to OpenRouter"
        )

        messages = (
            prompt_manager.build_chat_messages(
                prompt
            )
        )

        response = await self.client.chat.completions.create(

            model="openchat/openchat-7b:free",

            messages=messages,

            temperature=0.7
        )

        logger.info(
            "Received OpenRouter response"
        )

        return response.choices[0].message.content


openrouter_service = OpenRouterService()
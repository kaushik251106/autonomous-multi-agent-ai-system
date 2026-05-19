from openai import AsyncOpenAI

from app.core.config import settings

from app.core.logging_config import (
    logger
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

        response = await self.client.chat.completions.create(

            model="openchat/openchat-7b:free",

            messages=[

                {
                    "role": "system",
                    "content": (
                        "You are an advanced AI "
                        "research assistant."
                    )
                },

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            temperature=0.7
        )

        logger.info(
            "Received OpenRouter response"
        )

        return response.choices[0].message.content


openrouter_service = OpenRouterService()
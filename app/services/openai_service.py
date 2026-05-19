from openai import AsyncOpenAI

from app.core.config import settings

from app.core.logging_config import (
    logger
)


class OpenAIService:

    def __init__(self):

        self.client = AsyncOpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    async def generate_response(
        self,
        prompt: str
    ) -> str:

        logger.info(
            "Sending request to OpenAI"
        )

        response = await self.client.chat.completions.create(

            model="gpt-4.1-mini",

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
            "Received OpenAI response"
        )

        return response.choices[0].message.content
        

openai_service = OpenAIService()
from openai import AsyncOpenAI

from app.core.config import settings


class OpenAIService:

    def __init__(self):

        self.client = AsyncOpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    async def generate_response(
        self,
        prompt: str
    ) -> str:

        response = await self.client.chat.completions.create(

            model="gpt-4.1-mini",

            messages=[

                # =========================================
                # SYSTEM PROMPT
                # =========================================
                {
                    "role": "system",
                    "content": (
                        "You are an advanced AI "
                        "research assistant specialized "
                        "in AI engineering, software "
                        "architecture, and autonomous systems."
                    )
                },

                # =========================================
                # USER PROMPT
                # =========================================
                {
                    "role": "user",
                    "content": prompt
                }

            ],

            temperature=0.7
        )

        return response.choices[0].message.content


openai_service = OpenAIService()
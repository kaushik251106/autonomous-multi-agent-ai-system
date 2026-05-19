import google.generativeai as genai

from app.core.config import settings

from app.core.logging_config import (
    logger
)


class GeminiService:

    def __init__(self):

        genai.configure(
            api_key=settings.GEMINI_API_KEY
        )

        self.model = genai.GenerativeModel(
            "gemini-2.0-flash"
        )

    async def generate_response(
        self,
        prompt: str
    ) -> str:

        logger.info(
            "Sending request to Gemini"
        )

        response = self.model.generate_content(

            [
                (
                    "You are an advanced AI "
                    "research assistant specialized "
                    "in AI engineering and "
                    "autonomous systems."
                ),

                prompt
            ]
        )

        logger.info(
            "Received Gemini response"
        )

        return response.text


gemini_service = GeminiService()
from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    PROJECT_NAME: str = os.getenv(
        "PROJECT_NAME",
        "Autonomous Multi-Agent AI System"
    )

    API_V1_STR: str = "/api/v1"

    DEBUG: bool = os.getenv(
        "DEBUG",
        "True"
    ) == "True"

    OPENROUTER_API_KEY: str = os.getenv(
        "OPENROUTER_API_KEY",
        ""
    )


settings = Settings()
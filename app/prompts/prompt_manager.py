from app.prompts.base_prompt import (
    SYSTEM_PROMPT
)


class PromptManager:

    @staticmethod
    def build_chat_messages(
        user_prompt: str
    ):

        return [

            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": user_prompt
            }

        ]


prompt_manager = PromptManager()
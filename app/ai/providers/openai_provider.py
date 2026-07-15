from app.ai.base_ai import BaseAI


class OpenAIProvider(BaseAI):
    """OpenAI Provider."""

    def generate(self, prompt: str) -> str:
        return f"[OpenAI Placeholder] {prompt}"
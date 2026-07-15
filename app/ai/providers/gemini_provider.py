from app.ai.base_ai import BaseAI


class GeminiProvider(BaseAI):
    """Gemini AI Provider."""

    def generate(self, prompt: str) -> str:
        return f"[Gemini Placeholder] {prompt}"
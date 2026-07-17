from app.ai.provider import AIProvider

from app.ai.providers.groq_provider import GroqProvider


class AIManager:
    """Central AI manager for VishAI."""

    def __init__(self):
        self.providers = {
            AIProvider.GROQ: GroqProvider(),
        }

        self.current = AIProvider.GROQ

    def set_provider(self, provider: AIProvider):
        if provider not in self.providers:
            raise ValueError(f"Provider {provider} not registered.")

        self.current = provider

    def current_provider(self):
        return self.current.value

    def generate(self, prompt: str):
        return self.providers[self.current].generate(prompt)
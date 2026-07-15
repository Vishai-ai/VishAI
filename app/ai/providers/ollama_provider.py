import requests

from app.ai.base_ai import BaseAI


class OllamaProvider(BaseAI):
    """Ollama AI Provider."""

    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.model = "qwen3:4b"

    def generate(self, prompt: str) -> str:

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }

        response = requests.post(self.url, json=payload, timeout=120)

        response.raise_for_status()

        return response.json()["response"]
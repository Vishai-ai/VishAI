import requests

from app.ai.base_ai import BaseAI


class OllamaProvider(BaseAI):
    """Production-ready Ollama Provider."""

    def __init__(self, model="qwen3:4b"):
        self.url = "http://localhost:11434/api/generate"
        self.model = model

    def generate(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(
                self.url,
                json=payload,
                timeout=120
            )

            response.raise_for_status()

            data = response.json()

            return data.get("response", "").strip()

        except requests.exceptions.ConnectionError:
            return "Error: Ollama server is not running."

        except requests.exceptions.HTTPError as e:
            return f"HTTP Error: {e}"

        except Exception as e:
            return f"Unexpected Error: {e}"
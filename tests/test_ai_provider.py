from app.ai.providers.ollama_provider import OllamaProvider
from app.ai.providers.gemini_provider import GeminiProvider

ollama = OllamaProvider()
gemini = GeminiProvider()

print(ollama.generate("Hello"))

print(gemini.generate("Hello"))
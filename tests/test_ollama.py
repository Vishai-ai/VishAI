from app.ai.providers.ollama_provider import OllamaProvider

ai = OllamaProvider()

response = ai.generate("Introduce yourself in one sentence.")

print(response)
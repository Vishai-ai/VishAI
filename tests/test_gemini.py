from app.ai.providers.gemini_provider import GeminiProvider

ai = GeminiProvider()

response = ai.generate("Introduce yourself in one sentence.")

print(response)
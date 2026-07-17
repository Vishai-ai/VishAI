from app.ai.providers.groq_provider import GroqProvider

ai = GroqProvider()

print(ai.generate("Introduce yourself in one sentence."))
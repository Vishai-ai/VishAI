from app.ai.ai_manager import AIManager

ai = AIManager()

print("Current Provider :", ai.current_provider())

print()

response = ai.generate("Introduce yourself in one sentence.")

print(response)
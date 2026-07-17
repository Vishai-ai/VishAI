from app.ai.ai_manager import AIManager

manager = AIManager()

print(manager.current_provider())

print(manager.generate("Introduce yourself in one sentence."))
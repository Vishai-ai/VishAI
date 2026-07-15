from app.ai.ai_manager import AIManager
from app.ai.provider import AIProvider

manager = AIManager()

print(manager.current_provider())

manager.set_provider(AIProvider.GEMINI)

print(manager.current_provider())
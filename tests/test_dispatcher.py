from app.brain.intent import Intent
from app.ai.ai_manager import AIManager
from app.memory.memory_manager import MemoryManager
from app.automation.automation_manager import AutomationManager


class TaskDispatcher:
    """Dispatches tasks to the correct module."""

    def __init__(self):

        self.ai = AIManager()

        self.memory = MemoryManager()

        self.automation = AutomationManager()

    def dispatch(self, intent: Intent, prompt: str):

        if intent == Intent.AI_CHAT:
            return self.ai.generate(prompt)

        elif intent == Intent.MEMORY:
            return self.memory.add_note(prompt)

        elif intent == Intent.AUTOMATION:
            return self.automation.execute(prompt)

        return "Intent not implemented yet."
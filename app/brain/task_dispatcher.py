from app.brain.intent import Intent
from app.ai.ai_manager import AIManager


class TaskDispatcher:
    """Routes tasks to the correct module."""

    def __init__(self):
        self.ai = AIManager()

    def dispatch(self, intent: Intent, prompt: str):

        if intent == Intent.AI_CHAT:
            return self.ai.generate(prompt)

        if intent == Intent.CODING:
            return self.ai.generate(prompt)

        if intent == Intent.KNOWLEDGE:
            return self.ai.generate(prompt)

        if intent == Intent.MEMORY:
            return "[Memory Module Coming Soon]"

        if intent == Intent.AUTOMATION:
            return "[Automation Module Coming Soon]"

        return "Sorry, I don't know how to handle this request yet."
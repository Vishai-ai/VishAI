from app.brain.intent import Intent


class TaskDispatcher:
    """Routes tasks based on detected intent."""

    def dispatch(self, intent: Intent) -> str:

        if intent == Intent.AUTOMATION:
            return "Automation Module"

        elif intent == Intent.MEMORY:
            return "Memory Module"

        elif intent == Intent.CODING:
            return "Coding Module"

        elif intent == Intent.SEARCH:
            return "Search Module"

        elif intent == Intent.AI_CHAT:
            return "AI Chat Module"

        return "Unknown Module"
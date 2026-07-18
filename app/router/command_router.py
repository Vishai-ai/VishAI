from app.brain.intent import Intent


class CommandRouter:
    """
    Routes requests to the correct subsystem.
    """

    def route(self, intent: Intent) -> str:

        if intent == Intent.AI_CHAT:
            return "ai"

        elif intent == Intent.AUTOMATION:
            return "automation"

        elif intent == Intent.MEMORY:
            return "memory"

        elif intent == Intent.SEARCH:
            return "knowledge"

        elif intent == Intent.CODING:
            return "coding"

        return "unknown"
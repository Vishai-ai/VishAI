from app.brain.intent import Intent
from app.brain.intent_patterns import IntentPatterns


class IntentDetector:
    """Detects the user's intent."""

    def detect(self, text: str) -> Intent:

        text = text.lower()

        if any(word in text for word in IntentPatterns.AUTOMATION):
            return Intent.AUTOMATION

        if any(word in text for word in IntentPatterns.MEMORY):
            return Intent.MEMORY

        if any(word in text for word in IntentPatterns.CODING):
            return Intent.CODING

        if any(word in text for word in IntentPatterns.SEARCH):
            return Intent.SEARCH

        return Intent.AI_CHAT
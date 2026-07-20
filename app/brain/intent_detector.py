from app.brain.intent_patterns import IntentPatterns

class IntentDetector:
    """Detects the user's intent."""

    def detect(self, text: str) -> Intent:
        text = text.lower()

        if any(word in text for word in [
            "open",
            "close",
            "start",
            "launch",
            "run"
        ]):
            return Intent.AUTOMATION

        if any(word in text for word in [
            "remember",
            "save",
            "store",
            "forget"
        ]):
            return Intent.MEMORY

        if any(word in text for word in [
            "code",
            "python",
            "program",
            "debug",
            "function"
        ]):
            return Intent.CODING

        if any(word in text for word in [
            "search",
            "find",
            "look up",
            "google"
        ]):
            return Intent.SEARCH

        return Intent.AI_CHAT
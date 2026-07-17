from app.brain.intent import Intent


class IntentDetector:

    def detect(self, prompt: str) -> Intent:

        text = prompt.lower()

        if any(word in text for word in [
            "open",
            "close",
            "start",
            "launch"
        ]):
            return Intent.AUTOMATION

        if any(word in text for word in [
            "remember",
            "save",
            "store"
        ]):
            return Intent.MEMORY

        if any(word in text for word in [
            "code",
            "python",
            "bug",
            "error"
        ]):
            return Intent.CODING

        return Intent.AI_CHAT
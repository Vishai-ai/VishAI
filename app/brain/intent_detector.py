from app.core.logger import logger


class IntentDetector:
    """Detects user intent."""

    def detect(self, text: str) -> str:
        text = text.lower()

        if "remember" in text:
            return "memory_save"

        elif "what" in text:
            return "memory_recall"

        elif "task" in text:
            return "task"

        return "unknown"
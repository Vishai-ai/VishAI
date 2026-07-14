from app.core.logger import logger


class IntentDetector:
    """Detects user intent."""

    def detect(self, text: str) -> str:
        text = text.lower()

        if text.startswith("remember"):
            return "memory_save"

        elif text.startswith("what"):
            return "memory_recall"

        elif text.startswith("create task"):
            return "task"

        logger.info(f"Unknown intent: {text}")
        return "unknown"
from app.core.logger import logger


class IntentDetector:
    """Detects the user's intent."""

    def __init__(self):
        self.rules = {
            "remember": "memory_save",
            "what": "memory_recall",
            "open": "automation",
            "search": "search",
            "create task": "task",
            "learn": "knowledge",
        }

    def detect(self, text: str) -> str:
        text = text.lower().strip()

        for keyword, intent in self.rules.items():
            if text.startswith(keyword):
                logger.info(f"Detected Intent: {intent}")
                return intent

        logger.info("Detected Intent: unknown")
        return "unknown"
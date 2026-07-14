from app.core.logger import logger
from app.brain.intent_detector import IntentDetector


class BrainEngine:
    """Main decision engine."""

    def __init__(self, memory_manager):
        self.memory = memory_manager
        self.intent = IntentDetector()

        logger.info("Brain Engine Initialized")

    def think(self, user_input: str):

        intent = self.intent.detect(user_input)

        logger.info(f"Intent = {intent}")

        if intent == "memory_recall":
            return self.memory.get_user_name()

        return intent
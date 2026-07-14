from app.core.logger import logger
from app.brain.intent_detector import IntentDetector


class BrainEngine:
    """Main decision engine."""

    def __init__(self):
        self.intent = IntentDetector()

        logger.info("Brain Engine Initialized")

    def think(self, user_input: str):

        intent = self.intent.detect(user_input)

        logger.info(f"Intent = {intent}")

        return intent
from app.core.logger import logger
from app.brain.intent_detector import IntentDetector
from app.command.parser import CommandParser


class BrainEngine:
    """Main decision engine."""

    def __init__(self, memory_manager):
        self.memory = memory_manager
        self.intent = IntentDetector()
        self.parser = CommandParser()

        logger.info("Brain Engine Initialized")

    def think(self, user_input: str):
        intent = self.intent.detect(user_input)

        logger.info(f"Intent = {intent}")

        if intent == "memory_save":

            key, value = self.parser.parse_memory(user_input)

            if key:
                self.memory.set_fact(key, value)
                return f"Saved: {key} = {value}"

            return "Nothing to save."

        elif intent == "memory_recall":

            key = self.parser.parse_recall(user_input)

            if key:
                value = self.memory.get_fact(key)

                if value:
                    return value

                return f"I don't know your {key.replace('_', ' ')}."

            return "I couldn't understand your question."

        return "Unknown command."
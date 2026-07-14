from app.core.logger import logger
from app.brain.intent_detector import IntentDetector
from app.command.parser import CommandParser
from app.router.command_router import CommandRouter
from app.automation.automation_manager import AutomationManager
from app.nlu.pipeline import NLUPipeline


class BrainEngine:
    """Main decision engine."""

    def __init__(self, memory_manager):
        self.memory = memory_manager
        self.intent = IntentDetector()
        self.parser = CommandParser()
        self.router = CommandRouter()
        self.automation = AutomationManager()
        self.nlu = NLUPipeline()

        logger.info("Brain Engine Initialized")

    def think(self, user_input: str):
        user_input = self.nlu.process(user_input)
        intent = self.intent.detect(user_input)
        module = self.router.route(intent)

        logger.info(f"Module = {module}")
        logger.info(f"Intent = {intent}")

        if intent == "automation":
            return self.automation.execute(user_input)
        
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
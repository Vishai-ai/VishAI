from app.core.base_engine import BaseEngine

from app.conversation.conversation_manager import ConversationManager
from app.conversation.context_window import ContextWindow

from app.brain.intent_detector import IntentDetector
from app.brain.task_dispatcher import TaskDispatcher

from app.ai.ai_manager import AIManager


class BrainEngine(BaseEngine):
    """
    Central decision-making engine of VishAI.
    Responsible for:
    - Understanding user input
    - Detecting intent
    - Selecting the correct engine
    - Returning the final response
    """

    def __init__(self):
        super().__init__("Brain")

        self.conversation = ConversationManager()
        self.context = ContextWindow()

        self.detector = IntentDetector()
        self.dispatcher = TaskDispatcher()

        self.initialized = False

    def initialize(self) -> bool:
        self.initialized = True
        return True

    def shutdown(self):
        self.initialized = False

    def health(self):
        return {
            "engine": self.name,
            "initialized": self.initialized
        }

    def process(self, user_input: str):

        if not self.initialized:
            raise RuntimeError("BrainEngine is not initialized.")

        # Store user message
        self.conversation.add_user_message(user_input)

        # Detect intent
        intent = self.detector.detect(user_input)

        # Get correct engine
        engine = self.dispatcher.dispatch(intent)

        if engine is None:
            response = f"{intent.name} engine is not available."

        elif isinstance(engine, AIManager):
            response = engine.generate(user_input)

        else:
            # Future engines (Memory, Automation, Coding...)
            response = engine.execute(user_input)

        # Save response
        self.conversation.add_assistant_message(response)

        return response
from app.conversation.conversation_manager import ConversationManager
from app.conversation.context_window import ContextWindow
from app.brain.intent_detector import IntentDetector
from app.brain.task_dispatcher import TaskDispatcher
from app.brain.intent import Intent
from app.ai.ai_manager import AIManager


class BrainEngine:
    """Main brain of VishAI."""

    def __init__(self):

        self.conversation = ConversationManager()
        self.context = ContextWindow()
        self.detector = IntentDetector()
        self.dispatcher = TaskDispatcher()
        self.ai = AIManager()

    def process(self, user_input: str):

        # Save user message
        self.conversation.add_user_message(user_input)

        # Detect intent
        intent = self.detector.detect(user_input)

        # Dispatch task
        module = self.dispatcher.dispatch(intent)

        # AI Chat
        if intent == Intent.AI_CHAT:

            response = self.ai.generate(user_input)

        else:

            response = f"[{module}] Feature coming soon."

        # Save AI response
        self.conversation.add_assistant_message(response)

        return response
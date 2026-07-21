from app.core.base_engine import BaseEngine

from app.conversation.conversation_manager import ConversationManager
from app.conversation.context_window import ContextWindow

from app.ai.ai_manager import AIManager

from app.planner.planner_engine import PlannerEngine
from app.planner.plan_executor import PlanExecutor

from app.memory.memory_service import MemoryService
from app.knowledge.knowledge_service import KnowledgeService

from app.pipeline.request import Request

from app.intents.memory_intent import MemoryIntent
from app.intents.automation_intent import AutomationIntent
from app.intents.ai_intent import AIIntent

from app.brain.command_parser import CommandParser
from app.brain.brain_router import BrainRouter


class BrainEngine(BaseEngine):
    """
    VishAI Brain Engine

    Main Coordinator of VishAI.
    """

    def __init__(self):

        super().__init__("Brain")

        # ------------------------------------
        # Conversation
        # ------------------------------------

        self.conversation = ConversationManager()
        self.context = ContextWindow()

        # ------------------------------------
        # Services
        # ------------------------------------

        self.memory = MemoryService()
        self.knowledge = KnowledgeService()

        # ------------------------------------
        # Parser
        # ------------------------------------

        self.command_parser = CommandParser()

        # ------------------------------------
        # AI
        # ------------------------------------

        self.ai = AIManager()

        # ------------------------------------
        # Planner
        # ------------------------------------

        self.planner = PlannerEngine()
        self.executor = PlanExecutor()

        # ------------------------------------
        # Intents
        # ------------------------------------

        self.memory_intent = MemoryIntent(
            self.memory
        )

        self.automation_intent = AutomationIntent(
            self.planner,
            self.executor
        )

        self.ai_intent = AIIntent(
            self.ai,
            self.knowledge
        )

        # ------------------------------------
        # Router
        # ------------------------------------

        self.router = BrainRouter(
            self.memory_intent,
            self.automation_intent,
            self.ai_intent
        )

        # ------------------------------------
        # State
        # ------------------------------------

        self.initialized = False

    # ==================================================
    # Lifecycle
    # ==================================================

    def initialize(self):

        self.initialized = True
        return True

    def shutdown(self):

        self.initialized = False

    def health(self):

        return {
            "engine": self.name,
            "initialized": self.initialized
        }

    # ==================================================
    # Main Processing
    # ==================================================

    def process(self, user_input: str):

        if not self.initialized:

            raise RuntimeError(
                "BrainEngine is not initialized."
            )

        # ------------------------------------
        # Create Request
        # ------------------------------------

        request = Request(
            text=user_input
        )

        # ------------------------------------
        # Parse Command
        # ------------------------------------

        request.parsed_command = self.command_parser.parse(
            user_input
        )

        # ------------------------------------
        # Save Conversation
        # ------------------------------------

        self.conversation.add_user_message(
            user_input
        )

        # ------------------------------------
        # Save Memory
        # ------------------------------------

        self.memory.remember(
            user_input
        )

        # ------------------------------------
        # Route Request
        # ------------------------------------

        response = self.router.route(
            request
        )

        # ------------------------------------
        # Save Assistant Response
        # ------------------------------------

        self.conversation.add_assistant_message(
            response.message
        )

        return response
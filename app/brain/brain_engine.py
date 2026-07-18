from app.core.base_engine import BaseEngine

from app.conversation.conversation_manager import ConversationManager
from app.conversation.context_window import ContextWindow

from app.brain.intent_detector import IntentDetector

from app.ai.ai_manager import AIManager

from app.planner.planner_engine import PlannerEngine
from app.planner.plan_executor import PlanExecutor
from app.memory.memory_service import MemoryService
from app.knowledge.knowledge_service import KnowledgeService


class BrainEngine(BaseEngine):
    """
    VishAI Brain Engine

    Responsibilities
    ----------------
    - Receive user input
    - Store conversation
    - Detect intent
    - Decide AI or Automation
    - Execute plans
    - Return response
    """

    def __init__(self):
        super().__init__("Brain")

        # ---------------- Conversation ----------------

        self.conversation = ConversationManager()
        self.context = ContextWindow()
        self.memory = MemoryService()
        self.knowledge = KnowledgeService()

        # ---------------- Intelligence ----------------

        self.detector = IntentDetector()

        self.ai = AIManager()

        # ---------------- Planning ----------------

        self.planner = PlannerEngine()
        self.executor = PlanExecutor()

        # ---------------- State ----------------

        self.initialized = False

    # =====================================================
    # Engine Lifecycle
    # =====================================================

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

    # =====================================================
    # Main Processing
    # =====================================================

    def process(self, user_input: str):

        if not self.initialized:
            raise RuntimeError(
                "BrainEngine is not initialized."
            )

        # ----------------------------------------
        # Save User Message
        # ----------------------------------------

        self.conversation.add_user_message(
            user_input
        )
        
        # Store latest user message
        self.memory.remember(user_input)
        # ----------------------------------------
        # Detect Intent
        # ----------------------------------------

        intent = self.detector.detect(
            user_input
        )

        # ----------------------------------------
        # AI Conversation
        # ----------------------------------------

        if intent.name == "AI_CHAT":

            # 1. Search local knowledge
            knowledge = self.knowledge.search(user_input)

            if knowledge is not None:

                response = knowledge

            else:

                response = self.ai.generate(user_input)

        # ----------------------------------------
        # Automation / Planner
        # ----------------------------------------

        else:

            plan = self.planner.create_plan(
                user_input
            )

            results = self.executor.execute(
                plan
            )

            response = "\n".join(results)

        # ----------------------------------------
        # Save AI Response
        # ----------------------------------------

        self.conversation.add_assistant_message(
            response
        )

        return response
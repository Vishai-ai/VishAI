from app.core.base_engine import BaseEngine

from app.conversation.conversation_manager import ConversationManager
from app.conversation.context_window import ContextWindow

from app.brain.intent_detector import IntentDetector

from app.ai.ai_manager import AIManager

from app.planner.planner_engine import PlannerEngine
from app.planner.plan_executor import PlanExecutor

from app.memory.memory_service import MemoryService
from app.knowledge.knowledge_service import KnowledgeService

from app.pipeline.request import Request
from app.pipeline.response import Response
from app.intents.memory_intent import MemoryIntent
from app.intents.automation_intent import AutomationIntent
from app.intents.ai_intent import AIIntent


class BrainEngine(BaseEngine):
    """
    VishAI Brain Engine

    Responsibilities
    ----------------
    • Receive user input
    • Store conversation
    • Use local memory
    • Search local knowledge
    • Detect intent
    • Execute automation
    • Ask AI when required
    • Return Response object
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
        
        self.memory_intent = MemoryIntent(
            self.memory
        )
        
        

        # ------------------------------------
        # Intelligence
        # ------------------------------------

        self.detector = IntentDetector()
        self.ai = AIManager()

        # ------------------------------------
        # Planning
        # ------------------------------------

        self.planner = PlannerEngine()
        self.executor = PlanExecutor()
        self.automation_intent = AutomationIntent(

            self.planner,

            self.executor

        )

        # ------------------------------------
        # Intent Handlers
        # ------------------------------------

        self.ai_intent = AIIntent(
            self.ai,
            self.knowledge
        )

        # ------------------------------------
        # State
        # ------------------------------------

        self.initialized = False

    # =====================================================
    # Lifecycle
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

        # ------------------------------------
        # Request Object
        # ------------------------------------

        request = Request(
            text=user_input
        )
        
        response = self.memory_intent.handle(request)

        if response is not None:

            return response
        
        text = request.text.lower().strip()

        # ------------------------------------
        # Save Conversation
        # ------------------------------------

        self.conversation.add_user_message(user_input)

        # ------------------------------------
        # Save User Message
        # ------------------------------------

        self.memory.remember(user_input)

        
        # =====================================================
        # INTENT DETECTION
        # =====================================================

        intent = self.detector.detect(
            user_input
        )

        # =====================================================
        # AI CHAT
        # =====================================================

        if intent.name == "AI_CHAT":

            return self.ai_intent.handle(request)

        # =====================================================
        # AUTOMATION
        # =====================================================

        else:

            return self.automation_intent.handle(
                request
            )

        # ------------------------------------
        # Save Assistant Message
        # ------------------------------------

        self.conversation.add_assistant_message(
            response
        )

        # ------------------------------------
        # Response Object
        # ------------------------------------

        return Response(

            success=True,

            message=response

        )
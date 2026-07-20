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

from app.nlu.command_parser import CommandParser
from app.brain.command_parser import CommandParser
from app.brain.request_router import RequestRouter
from app.intents.browser_intent import BrowserIntent


class BrainEngine(BaseEngine):
    """
    VishAI Brain Engine

    Responsibilities
    ----------------
    - Receive user input
    - Store conversation
    - Store memory
    - Parse natural language
    - Detect intent
    - Execute automation
    - Ask AI
    - Return Response
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
        # NLU
        # ------------------------------------

        self.command_parser = CommandParser()

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

        # ------------------------------------
        # Intent Handlers
        # ------------------------------------

        self.memory_intent = MemoryIntent(
            self.memory
        )

        self.ai_intent = AIIntent(
            self.ai,
            self.knowledge
        )

        self.automation_intent = AutomationIntent(
            self.planner,
            self.executor
        )

        # ------------------------------------
        # State
        # ------------------------------------

        self.initialized = False

        # -----------------------------
        # Parser
        # -----------------------------

        self.parser = CommandParser()

        # -----------------------------
        # Router
        # -----------------------------
       # self.browser_intent = BrowserIntent()
        #self.router = RequestRouter(
         #   self.memory_intent,
          #  self.browser_intent,
           # self.automation_intent,
            #self.ai_intent
        )
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
        # Request
        # ------------------------------------

        request = Request(
            text=user_input
        )

        # ------------------------------------
        # NLU Parsing
        # ------------------------------------

        parsed_command = self.command_parser.parse(
            user_input
        )

        # Future use
        request.parsed_command = parsed_command

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
        # Memory Intent
        # ------------------------------------

        response = self.memory_intent.handle(
            request
        )

        if response is not None:

            self.conversation.add_assistant_message(
                response.message
            )

            return response

        # ------------------------------------
        # Intent Detection
        # ------------------------------------

        parsed = self.parser.parse(user_input)

        # अगर Parser ने Action पहचाना है
        if parsed["action"]:

            plan = self.planner.create_plan(parsed)

            results = self.executor.execute(plan)

            return Response(
                success=True,
                message="\n".join(results)
             )

        # नहीं तो Router को भेजो
        return self.router.route(request)
        # ------------------------------------
        # AI
        # ------------------------------------

        if intent.name == "AI_CHAT":

            response = self.ai_intent.handle(
                request
            )

        # ------------------------------------
        # Automation
        # ------------------------------------

        else:

            response = self.automation_intent.handle(
                request
            )

        # ------------------------------------
        # Save Assistant Response
        # ------------------------------------

        self.conversation.add_assistant_message(
            response.message
        )

        return response
from app.core.service_registry import ServiceRegistry

from app.ai.ai_manager import AIManager

from app.memory.memory_service import MemoryService

from app.knowledge.knowledge_service import KnowledgeService

from app.planner.planner_engine import PlannerEngine

from app.planner.plan_executor import PlanExecutor


class VishAIApplication:

    """
    Initializes every core service.

    """

    def __init__(self):

        self.registry = ServiceRegistry()

    def initialize(self):

        self.registry.register(

            "ai",

            AIManager()

        )

        self.registry.register(

            "memory",

            MemoryService()

        )

        self.registry.register(

            "knowledge",

            KnowledgeService()

        )

        self.registry.register(

            "planner",

            PlannerEngine()

        )

        self.registry.register(

            "executor",

            PlanExecutor()

        )

        return self.registry
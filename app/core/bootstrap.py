from app.core.service_registry import ServiceRegistry

from app.ai.ai_manager import AIManager
from app.memory.memory_service import MemoryService
from app.knowledge.knowledge_service import KnowledgeService

from app.planner.planner_engine import PlannerEngine
from app.planner.plan_executor import PlanExecutor

from app.automation.command_executor import CommandExecutor


class Bootstrap:
    """
    Initializes all VishAI core services.
    """

    def __init__(self):

        self.registry = ServiceRegistry()

        self.initialized = False

    def initialize(self):

        if self.initialized:
            return self.registry

        # AI
        self.registry.register(
            "ai",
            AIManager()
        )

        # Memory
        self.registry.register(
            "memory",
            MemoryService()
        )

        # Knowledge
        self.registry.register(
            "knowledge",
            KnowledgeService()
        )

        # Planner
        self.registry.register(
            "planner",
            PlannerEngine()
        )

        self.registry.register(
            "plan_executor",
            PlanExecutor()
        )

        # Automation
        self.registry.register(
            "command_executor",
            CommandExecutor()
        )

        self.initialized = True

        return self.registry
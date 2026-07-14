from app.core.logger import logger
from app.memory.memory_manager import MemoryManager
from app.knowledge.knowledge_manager import KnowledgeManager
from app.tasks.task_manager import TaskManager


class VishAIKernel:
    """Core kernel of VishAI."""

    def __init__(self):
        logger.info("Initializing VishAI Kernel...")

        self.memory = MemoryManager()
        self.knowledge = KnowledgeManager()
        self.tasks = TaskManager()

        logger.info(f"Welcome {self.memory.get_user_name()}")
        logger.info("Kernel Ready")
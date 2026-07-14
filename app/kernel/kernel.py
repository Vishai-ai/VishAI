from app.core.logger import logger
from app.memory.memory_manager import MemoryManager
from app.knowledge.knowledge_manager import KnowledgeManager


class VishAIKernel:
    """Core kernel of VishAI."""

    def __init__(self):
        logger.info("Initializing VishAI Kernel...")

        self.memory = MemoryManager()
        self.knowledge = KnowledgeManager()

        logger.info(f"Welcome {self.memory.get_user_name()}")

        logger.info("Kernel Ready")
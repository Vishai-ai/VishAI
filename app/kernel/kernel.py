from app.core.logger import logger
from app.memory.memory_manager import MemoryManager


class VishAIKernel:

    def __init__(self):
        logger.info("Initializing VishAI Kernel...")

        self.memory = MemoryManager()

        logger.info(f"Welcome {self.memory.get_user_name()}")

        logger.info("Kernel Ready")
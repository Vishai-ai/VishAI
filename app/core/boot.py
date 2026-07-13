from app.config.settings import APP_NAME, VERSION
from app.core.logger import logger
from app.memory.memory_manager import MemoryManager


def boot():
    logger.info("=" * 40)
    logger.info(f"Booting {APP_NAME}")
    logger.info(f"Version : {VERSION}")

    memory = MemoryManager()

    logger.info("Boot Complete")
    logger.info("=" * 40)
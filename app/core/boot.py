from app.config.settings import APP_NAME, VERSION
from app.core.logger import logger
from app.kernel.kernel import VishAIKernel


def boot():
    logger.info("=" * 40)
    logger.info(f"Booting {APP_NAME}")
    logger.info(f"Version : {VERSION}")

    kernel = VishAIKernel()

    logger.info("System Ready")
    logger.info("=" * 40)
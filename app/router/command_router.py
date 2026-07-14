from app.core.logger import logger


class CommandRouter:
    """Routes commands to the correct module."""

    def route(self, intent: str) -> str:
        routes = {
            "memory_save": "memory",
            "memory_recall": "memory",
            "automation": "automation",
            "knowledge": "knowledge",
        }

        module = routes.get(intent, "unknown")

        logger.info(f"Routing -> {module}")

        return module
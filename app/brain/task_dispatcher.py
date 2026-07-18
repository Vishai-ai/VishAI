from app.brain.intent import Intent
from app.ai.ai_manager import AIManager


class TaskDispatcher:
    """
    Dispatches intents to the correct engine.
    """

    def __init__(self):

        self.ai = AIManager()

        # Future
        self.memory = None
        self.automation = None
        self.search = None
        self.coding = None

    def dispatch(self, intent: Intent):

        routes = {

            Intent.AI_CHAT: self.ai,

            Intent.AUTOMATION: self.automation,

            Intent.MEMORY: self.memory,

            Intent.CODING: self.coding,

            Intent.SEARCH: self.search,

        }

        return routes.get(intent)
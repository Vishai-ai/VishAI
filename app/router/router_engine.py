from app.brain.intent import Intent


class RouterEngine:
    """
    Decides which engine should execute the task.
    """

    def route(self, intent: Intent):

        routes = {

            Intent.AI_CHAT: "AI",

            Intent.AUTOMATION: "Automation",

            Intent.MEMORY: "Memory",

            Intent.CODING: "Coding",

            Intent.SEARCH: "Search"

        }

        return routes.get(intent, "Unknown")
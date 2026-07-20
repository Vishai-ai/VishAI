from app.intents.memory_intent import MemoryIntent
from app.intents.browser_intent import BrowserIntent
from app.intents.automation_intent import AutomationIntent
from app.intents.ai_intent import AIIntent


class RequestRouter:
    """
    Routes a request to the correct intent handler.
    """

    def __init__(
        self,
        memory_intent,
        browser_intent,
        automation_intent,
        ai_intent
    ):

        self.memory_intent = memory_intent
        self.browser_intent = browser_intent
        self.automation_intent = automation_intent
        self.ai_intent = ai_intent

    def route(self, request):

        # Memory
        response = self.memory_intent.handle(request)
        if response is not None:
            return response

        # Browser
        response = self.browser_intent.handle(request)
        if response is not None:
            return response

        text = request.text.lower()

        # Desktop Automation
        if any(word in text for word in [
            "open",
            "launch",
            "start",
            "run",
            "execute"
        ]):
            return self.automation_intent.handle(request)

        # Default
        return self.ai_intent.handle(request)
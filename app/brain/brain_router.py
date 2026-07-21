class BrainRouter:
    """
    Routes requests to the correct intent.
    """

    def __init__(self,
                 memory_intent,
                 automation_intent,
                 ai_intent):

        self.memory_intent = memory_intent
        self.automation_intent = automation_intent
        self.ai_intent = ai_intent

    def route(self, request):

        # -----------------------
        # Memory
        # -----------------------

        response = self.memory_intent.handle(request)

        if response is not None:
            return response

        # -----------------------
        # Automation
        # -----------------------

        parsed = getattr(request, "parsed_command", None)

        if parsed:

            if parsed.get("action") is not None:

                return self.automation_intent.handle(request)

        # -----------------------
        # AI
        # -----------------------

        return self.ai_intent.handle(request)
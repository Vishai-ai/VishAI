class BrainRouter:
    """
    Routes requests to the correct intent.
    """

    def __init__(
        self,
        memory_intent,
        automation_intent,
        ai_intent,
    ):

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

        print("\n===== ROUTER DEBUG =====")
        print(parsed)
        print("========================")

        if parsed:

            action = parsed.get("action")

            print("ACTION =", action)

            if action is not None:

                print(">>> Routing to AutomationIntent")

                return self.automation_intent.handle(request)

        # -----------------------
        # AI
        # -----------------------

        print(">>> Routing to AIIntent")

        return self.ai_intent.handle(request)
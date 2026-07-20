from app.capabilities.capability import Capability


class AICapability(Capability):

    def __init__(self, ai_intent):

        super().__init__("AI")

        self.intent = ai_intent

    def can_handle(self, request):

        return True

    def handle(self, request):

        return self.intent.handle(request)
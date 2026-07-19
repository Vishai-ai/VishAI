from app.capabilities.capability import Capability


class MemoryCapability(Capability):

    def __init__(self, memory_intent):

        super().__init__("Memory")

        self.intent = memory_intent

    def can_handle(self, request):

        text = request.text.lower()

        return (

            text.startswith("my name is")

            or

            text.startswith("remember ")

            or

            text.startswith("what is")

        )

    def handle(self, request):

        return self.intent.handle(request)
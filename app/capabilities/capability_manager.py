class CapabilityManager:

    def __init__(self):

        self.capabilities = []

    def register(self, capability):

        self.capabilities.append(capability)

    def unregister(self, name):

        self.capabilities = [

            c for c in self.capabilities

            if c.name != name

        ]

    def get(self, name):

        for capability in self.capabilities:

            if capability.name == name:

                return capability

        return None

    def handle(self, request):

        for capability in self.capabilities:

            if capability.can_handle(request):

                return capability.handle(request)

        return None

    def all(self):

        return self.capabilities
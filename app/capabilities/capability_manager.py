class CapabilityManager:

    def __init__(self):

        self.capabilities = []

    def register(self, capability):

        self.capabilities.append(capability)

    def all(self):

        return self.capabilities
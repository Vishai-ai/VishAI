class ServiceRegistry:
    """
    Central registry for all VishAI services.

    This prevents tight coupling between modules.
    """

    def __init__(self):

        self._services = {}

    def register(self, name: str, service):

        self._services[name] = service

    def get(self, name: str):

        return self._services.get(name)

    def exists(self, name: str):

        return name in self._services

    def remove(self, name: str):

        if name in self._services:

            del self._services[name]

    def clear(self):

        self._services.clear()

    def all(self):

        return self._services
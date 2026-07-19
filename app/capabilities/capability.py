from abc import ABC, abstractmethod


class Capability(ABC):
    """
    Base class for every VishAI capability.
    """

    def __init__(self, name: str):

        self.name = name

    @abstractmethod
    def can_handle(self, request):

        pass

    @abstractmethod
    def handle(self, request):

        pass
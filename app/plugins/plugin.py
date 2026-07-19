from abc import ABC, abstractmethod


class Plugin(ABC):
    """
    Base class for all VishAI plugins.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass

    @abstractmethod
    def execute(self, command: str):
        pass
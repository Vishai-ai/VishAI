from abc import ABC, abstractmethod


class BasePlugin(ABC):
    """Base class for every VishAI plugin."""

    @abstractmethod
    def execute(self, command: str):
        pass
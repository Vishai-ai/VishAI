from abc import ABC, abstractmethod


class BaseSkill(ABC):
    """Base class for every VishAI skill."""

    @abstractmethod
    def execute(self, command: str):
        pass
from abc import ABC, abstractmethod


class BaseSkill(ABC):
    """
    Base class for every VishAI skill.
    """

    @abstractmethod
    def can_handle(self, text: str) -> bool:
        pass

    @abstractmethod
    def execute(self, text: str):
        pass
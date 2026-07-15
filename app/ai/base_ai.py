from abc import ABC, abstractmethod


class BaseAI(ABC):
    """Base interface for every AI provider."""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass
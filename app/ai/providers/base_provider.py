from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """Base class for all AI providers."""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a response."""
        pass
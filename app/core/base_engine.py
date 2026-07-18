from abc import ABC, abstractmethod


class BaseEngine(ABC):
    """
    Base class for all VishAI engines.

    Every engine must implement:
    - initialize()
    - shutdown()
    - health()
    """

    def __init__(self, name: str):
        self.name = name
        self.initialized = False

    @abstractmethod
    def initialize(self) -> bool:
        """Initialize the engine."""
        pass

    @abstractmethod
    def shutdown(self) -> None:
        """Shutdown the engine."""
        pass

    @abstractmethod
    def health(self) -> dict:
        """Return engine health information."""
        pass
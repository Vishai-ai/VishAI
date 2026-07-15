class VishAIError(Exception):
    """Base exception for VishAI."""
    pass


class MemoryError(VishAIError):
    """Raised when memory operation fails."""
    pass


class AutomationError(VishAIError):
    """Raised when automation fails."""
    pass


class ConfigurationError(VishAIError):
    """Raised when configuration is invalid."""
    pass
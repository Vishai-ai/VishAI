class BaseSkill:
    """Base class for every VishAI skill."""

    def execute(self, command: str):
        raise NotImplementedError
from dataclasses import dataclass, field

from app.brain.command_step import CommandStep


@dataclass
class ParsedCommand:
    """
    Represents one parsed user command.
    """

    original_text: str

    steps: list[CommandStep] = field(default_factory=list)

    def add_step(self, step: CommandStep):

        self.steps.append(step)
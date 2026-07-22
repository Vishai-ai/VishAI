from dataclasses import dataclass


@dataclass
class CommandStep:
    """
    Represents one executable step.
    """

    action: str

    target: str = ""

    value: str = ""
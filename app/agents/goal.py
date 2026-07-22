from dataclasses import dataclass


@dataclass
class Goal:
    """
    Represents the user's final goal.
    """

    text: str
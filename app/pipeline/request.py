from dataclasses import dataclass, field


@dataclass
class Request:
    """
    Represents a user request flowing through VishAI.
    """

    text: str

    intent: str = ""

    source: str = "user"

    parsed_command: dict = field(default_factory=dict)

    metadata: dict = field(default_factory=dict)
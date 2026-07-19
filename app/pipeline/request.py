from dataclasses import dataclass


@dataclass
class Request:
    """
    Represents one user request.
    """

    text: str
    intent: str = ""
    source: str = "user"
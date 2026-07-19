from dataclasses import dataclass


@dataclass
class Response:
    """
    Represents VishAI response.
    """

    success: bool
    message: str
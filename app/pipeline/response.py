from dataclasses import dataclass, field


@dataclass
class Response:
    """
    Standard response object.
    """

    success: bool

    message: str

    data: dict = field(default_factory=dict)
from dataclasses import dataclass
from typing import Any


@dataclass
class Task:
    """
    Represents one executable task.
    """

    action: str

    target: str = ""

    value: Any = None
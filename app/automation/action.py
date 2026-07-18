from dataclasses import dataclass
from typing import Optional


@dataclass
class Action:
    """
    Represents one executable action.
    """

    action: str

    target: Optional[str] = None

    value: Optional[str] = None
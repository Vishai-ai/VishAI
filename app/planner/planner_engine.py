from dataclasses import dataclass
from typing import List

from app.core.base_engine import BaseEngine


@dataclass
class Plan:

    goal: str

    steps: List[str]


class PlannerEngine(BaseEngine):
    """
    Converts a user goal into executable steps.
    """

    def __init__(self):
        super().__init__("Planner")

    def initialize(self) -> bool:

        self.initialized = True
        return True

    def shutdown(self):

        self.initialized = False

    def health(self):

        return {
            "engine": self.name,
            "initialized": self.initialized
        }

    def create_plan(self, goal: str) -> Plan:

        text = goal.lower()

        steps = []

        if "chrome" in text:

            steps.append("Open Chrome")

        if "google" in text:

            steps.append("Open Google")

        if "youtube" in text:

            steps.append("Open YouTube")

        if "search" in text:

            steps.append("Perform Search")

        if "close" in text:

            steps.append("Close Application")

        if not steps:

            steps.append("Think about the request")

        return Plan(
            goal=goal,
            steps=steps
        )
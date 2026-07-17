from dataclasses import dataclass


@dataclass
class Plan:

    goal: str

    steps: list[str]


class PlannerEngine:

    """
    Breaks one user request into executable steps.
    """

    def create_plan(self, user_input: str) -> Plan:

        return Plan(
            goal=user_input,
            steps=[user_input]
        )
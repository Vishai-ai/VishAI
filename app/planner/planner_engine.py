from app.planner.plan import Plan
from app.planner.task import Task


class PlannerEngine:
    """
    Converts user requests into executable plans.
    """

    def create_plan(self, command: str) -> Plan:

        text = command.lower()

        plan = Plan()

        # ---------------- Notepad ----------------

        if "notepad" in text:

            plan.add(
                Task(
                    action="open_app",
                    target="notepad"
                )
            )

        # ---------------- Calculator ----------------

        elif "calculator" in text or "calc" in text:

            plan.add(
                Task(
                    action="open_app",
                    target="calculator"
                )
            )

        # ---------------- Paint ----------------

        elif "paint" in text:

            plan.add(
                Task(
                    action="open_app",
                    target="paint"
                )
            )

        # ---------------- CMD ----------------

        elif "cmd" in text:

            plan.add(
                Task(
                    action="open_app",
                    target="cmd"
                )
            )

        else:

            plan.add(
                Task(
                    action="chat",
                    value=command
                )
            )

        return plan
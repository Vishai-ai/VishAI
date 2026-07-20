from app.planner.plan import Plan
from app.planner.task import Task


class PlannerEngine:
    """
    Creates execution plans from parsed commands.
    """

    def create_plan(self, parsed):

        plan = Plan()

        action = parsed.get("action")

        target = parsed.get("target")

        # -----------------------------------------
        # Open Application
        # -----------------------------------------

        if action == "open_app" and target:

            plan.add(

                Task(

                    action="open_app",

                    target=target

                )

            )

        return plan
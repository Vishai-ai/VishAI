from app.planner.plan import Plan
from app.planner.task_factory import TaskFactory


class PlannerEngine:
    """
    Creates execution plans from parsed commands.
    Supports multi-step plans.
    """

    def create_plan(self, parsed):

        plan = Plan()

        action = parsed.get("action")
        target = parsed.get("target")
        value = parsed.get("value")
        text = parsed.get("text", "")

        # ------------------------------------
        # Open Desktop Application
        # ------------------------------------

        if action == "open_app":

            plan.add(
                TaskFactory.open_app(target)
            )

            return plan

        # ------------------------------------
        # Google Search
        # ------------------------------------

        if action == "search":

            plan.add(
                TaskFactory.browser(
                    "google",
                    value
                )
            )

            return plan

        # ------------------------------------
        # YouTube Search
        # ------------------------------------

        if action == "youtube_search":

            plan.add(
                TaskFactory.browser(
                    "youtube",
                    value
                )
            )

            return plan

        # ------------------------------------
        # Open Site
        # ------------------------------------

        if action == "open_site":

            plan.add(
                TaskFactory.browser(
                    target
                )
            )

            return plan

        # ------------------------------------
        # Multi-step:
        # open notepad and type hello
        # ------------------------------------

        if action == "open_and_type":

            plan.add(
                TaskFactory.open_app(target)
            )

            plan.add(
                TaskFactory.wait(2)
            )

            plan.add(
                TaskFactory.type_text(value)
            )

            return plan

        # ------------------------------------
        # Default
        # ------------------------------------

        plan.add(
            TaskFactory.browser(
                "google",
                text
            )
        )

        return plan
from app.planner.plan import Plan
from app.planner.task import Task


class PlannerEngine:
    """
    Converts user requests into executable plans.
    """

    def create_plan(self, command: str) -> Plan:

        text = command.lower().strip()

        plan = Plan()

        trigger_words = [

            "open",
            "launch",
            "start",
            "run",
            "execute"

        ]

        if any(word in text for word in trigger_words):

            words = text.split(maxsplit=1)

            if len(words) >= 2:

                app = words[1].strip()
                plan.add(

                    Task(

                        action="open_app",

                        target=app

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
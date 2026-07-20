from app.planner.task import Task
from app.planner.task_sequence import TaskSequence


class MultiStepPlanner:
    """
    Converts one user command into multiple executable tasks.
    """

    def create(self, command: str):

        text = command.lower()

        sequence = TaskSequence()

        # -----------------------------
        # Open Notepad and Type
        # -----------------------------

        if "open notepad" in text:

            sequence.add(
                Task(
                    action="open_app",
                    target="notepad"
                )
            )

            if "type" in text:

                message = command.split("type", 1)[1].strip()

                sequence.add(
                    Task(
                        action="wait",
                        value=1
                    )
                )

                sequence.add(
                    Task(
                        action="type",
                        value=message
                    )
                )

        return sequence
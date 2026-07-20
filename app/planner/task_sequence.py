from app.planner.task import Task


class TaskSequence:
    """
    Represents a sequence of executable tasks.
    """

    def __init__(self):

        self.tasks = []

    def add(self, task: Task):

        self.tasks.append(task)

    def extend(self, tasks):

        self.tasks.extend(tasks)

    def __iter__(self):

        return iter(self.tasks)

    def __len__(self):

        return len(self.tasks)

    def is_empty(self):

        return len(self.tasks) == 0

    def clear(self):

        self.tasks.clear()
from app.planner.task import Task


class Plan:

    def __init__(self):

        self.tasks = []

    def add(self, task: Task):

        self.tasks.append(task)

    def clear(self):

        self.tasks.clear()

    def __iter__(self):

        return iter(self.tasks)

    def __len__(self):

        return len(self.tasks)
from collections import deque


class TaskScheduler:
    """
    Schedules tasks in execution order.
    """

    def __init__(self):

        self.queue = deque()

    # -------------------------

    def add_task(self, task):

        self.queue.append(task)

    # -------------------------

    def add_tasks(self, tasks):

        for task in tasks:

            self.queue.append(task)

    # -------------------------

    def next_task(self):

        if self.queue:

            return self.queue.popleft()

        return None

    # -------------------------

    def has_tasks(self):

        return len(self.queue) > 0

    # -------------------------

    def clear(self):

        self.queue.clear()

    # -------------------------

    def size(self):

        return len(self.queue)
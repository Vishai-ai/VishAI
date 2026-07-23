from app.agent.goal import Goal


class GoalManager:
    """
    Stores and manages the current goal.
    """

    def __init__(self):

        self.current_goal = None

    # -------------------------

    def set_goal(self, text):

        self.current_goal = Goal(text)

        return self.current_goal

    # -------------------------

    def get_goal(self):

        return self.current_goal

    # -------------------------

    def clear(self):

        self.current_goal = None

    # -------------------------

    def has_goal(self):

        return self.current_goal is not None
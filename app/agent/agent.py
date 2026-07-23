from app.agent.agent_state import AgentState
from app.agent.task_queue import TaskQueue
from app.agent.execution_context import ExecutionContext


class Agent:

    def __init__(self):

        self.state = AgentState.IDLE

        self.queue = TaskQueue()

        self.context = ExecutionContext()

        self.goal = None

    # ---------------------

    def assign_goal(self, goal):

        self.goal = goal

        self.state = AgentState.PLANNING

    # ---------------------

    def start_execution(self):

        self.state = AgentState.EXECUTING

    # ---------------------

    def complete(self):

        self.state = AgentState.FINISHED

    # ---------------------

    def fail(self):

        self.state = AgentState.FAILED
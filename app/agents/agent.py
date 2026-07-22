from app.agent.agent_state import AgentState
from app.agent.task_queue import TaskQueue
from app.agent.execution_context import ExecutionContext


class Agent:

    def __init__(self):

        self.state = AgentState.IDLE

        self.queue = TaskQueue()

        self.context = ExecutionContext()

    def start(self):

        self.state = AgentState.PLANNING

    def execute(self):

        self.state = AgentState.EXECUTING

    def finish(self):

        self.state = AgentState.FINISHED
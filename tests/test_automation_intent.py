from app.intents.automation_intent import AutomationIntent
from app.planner.planner_engine import PlannerEngine
from app.planner.plan_executor import PlanExecutor
from app.pipeline.request import Request

planner = PlannerEngine()
executor = PlanExecutor()

intent = AutomationIntent(
    planner,
    executor
)

response = intent.handle(
    Request("open notepad")
)

print(response.message)
from app.planner.planner_engine import PlannerEngine
from app.planner.plan_executor import PlanExecutor


planner = PlannerEngine()

executor = PlanExecutor()


plan = planner.create_plan(

    "Open Notepad"

)


result = executor.execute(plan)

print(result)
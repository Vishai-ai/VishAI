from app.planner.planner_engine import PlannerEngine

planner = PlannerEngine()

plan = planner.create_plan(
    "Open Chrome"
)

print(plan.goal)

print(plan.steps)
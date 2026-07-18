from app.planner.planner_engine import PlannerEngine


planner = PlannerEngine()

planner.initialize()

plan = planner.create_plan(
    "Open Chrome and search Python on YouTube"
)

print("Goal:")
print(plan.goal)

print()

print("Steps:")

for i, step in enumerate(plan.steps, start=1):
    print(f"{i}. {step}")
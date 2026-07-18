from app.planner.planner_engine import PlannerEngine

planner = PlannerEngine()

plan = planner.create_plan(

    "Open Notepad"

)

print("Tasks:", len(plan))

for task in plan:

    print(task)
from app.planner.multi_step_planner import MultiStepPlanner

planner = MultiStepPlanner()

plan = planner.create(

    "open notepad and type Hello VishAI"

)

for task in plan:

    print(task)
from app.planner.plan import Plan
from app.planner.task import Task

plan = Plan()

plan.add(Task("open_app", "notepad"))

plan.add(Task("type_text", value="Hello VishAI"))

print("Total Tasks:", len(plan))

for task in plan:

    print(task)
    
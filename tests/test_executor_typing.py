from app.planner.plan import Plan
from app.planner.plan_executor import PlanExecutor
from app.planner.task import Task

executor = PlanExecutor()

plan = Plan()

# Step 1 - Open Notepad
plan.add(
    Task(
        action="open_app",
        target="notepad"
    )
)

# Step 2 - Wait 3 seconds
plan.add(
    Task(
        action="wait",
        value=3
    )
)

# Step 3 - Type text
plan.add(
    Task(
        action="type",
        value="Hello VishAI"
    )
)

results = executor.execute(plan)

print("\nResults:\n")

for result in results:
    print(result)
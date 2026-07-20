from app.brain.command_parser import CommandParser
from app.planner.planner_engine import PlannerEngine

parser = CommandParser()

planner = PlannerEngine()

parsed = parser.parse(

    "please open chrome"

)

plan = planner.create_plan(parsed)

for task in plan:

    print(task)
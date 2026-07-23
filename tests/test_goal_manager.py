from app.goals.goal_manager import GoalManager

manager = GoalManager()

goal = manager.set_goal(

    "Create Python Project"

)

print(goal)

print(manager.has_goal())

print(manager.get_goal())

manager.clear()

print(manager.has_goal())
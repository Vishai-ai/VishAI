from app.tasks.task_manager import TaskManager

manager = TaskManager()

manager.add_task("Study Physics")
manager.add_task("Practice Python")

for task in manager.list_tasks():
    print(task)

manager.complete_task(1)

print("-" * 40)

for task in manager.list_tasks():
    print(task)
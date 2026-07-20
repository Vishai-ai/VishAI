from app.planner.task_sequence import TaskSequence
from app.planner.task import Task

sequence = TaskSequence()

sequence.add(Task(
    action="open_app",
    target="notepad"
))

sequence.add(Task(
    action="type",
    value="Hello VishAI"
))

print(len(sequence))

for task in sequence:
    print(task)
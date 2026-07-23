from app.scheduler.task_scheduler import TaskScheduler

scheduler = TaskScheduler()

scheduler.add_task("Open Chrome")
scheduler.add_task("Search Python")
scheduler.add_task("Open First Result")

while scheduler.has_tasks():

    print(scheduler.next_task())
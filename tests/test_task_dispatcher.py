from app.brain.task_dispatcher import TaskDispatcher
from app.brain.intent import Intent

dispatcher = TaskDispatcher()

print(dispatcher.dispatch(Intent.AUTOMATION))
print(dispatcher.dispatch(Intent.MEMORY))
print(dispatcher.dispatch(Intent.CODING))
print(dispatcher.dispatch(Intent.SEARCH))
print(dispatcher.dispatch(Intent.AI_CHAT))
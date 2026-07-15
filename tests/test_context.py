from app.context.context_manager import ContextManager

context = ContextManager()

context.update("Open Chrome", "chrome")

print(context.get_last_command())
print(context.get_last_app())

context.update("Open Calculator", "calculator")

print(context.get_last_command())
print(context.get_last_app())
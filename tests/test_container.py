from app.core.container import AppContainer

container = AppContainer()

print(type(container.memory).__name__)
print(type(container.automation).__name__)
print(type(container.brain).__name__)
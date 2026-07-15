from app.core.container import AppContainer

container = AppContainer()

memory = container.plugins.get_plugin("memory")
automation = container.plugins.get_plugin("automation")

print(memory.execute(""))
print(automation.execute("Open Calculator"))
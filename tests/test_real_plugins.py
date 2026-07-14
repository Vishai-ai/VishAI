from app.plugins.plugin_manager import PluginManager

manager = PluginManager()

memory = manager.get_plugin("memory")
automation = manager.get_plugin("automation")

print("Memory:")
print(memory.execute(""))

print("-" * 40)

print("Automation:")
print(automation.execute("Open Calculator"))
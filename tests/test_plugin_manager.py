from app.plugins.plugin_manager import PluginManager

manager = PluginManager()

memory = manager.get_plugin("memory")
automation = manager.get_plugin("automation")

print(memory.execute("remember my name"))
print(automation.execute("open chrome"))
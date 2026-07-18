from app.automation.app_registry import AppRegistry

registry = AppRegistry()

print(registry.exists("notepad"))

print(registry.get("notepad"))

print(registry.all_apps())
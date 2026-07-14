from app.automation.automation_manager import AutomationManager

automation = AutomationManager()

tests = [
    "Open Calculator",
    "Open Notepad",
    "Open Chrome",
    "Open VS Code",
]

for command in tests:
    print(automation.execute(command))
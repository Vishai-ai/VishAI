from app.automation.automation_manager import AutomationManager

automation = AutomationManager()

tests = [
    "Open Calculator",
    "Open Notepad",
    "Open Chrome",
    "Open VS Code",
    "Open youtube.com",
    "Open github.com",
]

for command in tests:
    print(command)
    print(automation.execute(command))
    print("-" * 30)
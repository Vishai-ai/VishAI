from app.automation.automation_engine import AutomationEngine

automation = AutomationEngine()

automation.initialize()

print(automation.health())

automation.open_notepad()

automation.wait(1.5)

automation.type_text("Hello Vishal!")

automation.wait(1)

automation.press("enter")

automation.type_text("Welcome to VishAI.")

print("Automation Test Completed.")
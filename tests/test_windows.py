from app.automation.windows import WindowsAutomation

windows = WindowsAutomation()

print(windows.open_calculator())
print(windows.open_notepad())
print(windows.open_chrome())
print(windows.open_vscode())
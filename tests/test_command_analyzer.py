from app.automation.command_analyzer import CommandAnalyzer

analyzer = CommandAnalyzer()

tests = [
    "Open Calculator",
    "Open Notepad",
    "Open Chrome",
    "Open VS Code",
    "Open youtube.com",
    "Open github.com",
    "Open Something",
]

for test in tests:
    print(test, "->", analyzer.analyze(test))
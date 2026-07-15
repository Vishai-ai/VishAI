from app.history.command_history import CommandHistory

history = CommandHistory()

history.add("Open Chrome")
history.add("Open Calculator")
history.add("Remember my city is Lucknow")

for item in history.list():
    print(item)

print("-" * 40)

history.clear()

print(history.list())
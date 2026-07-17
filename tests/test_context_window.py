from app.conversation.context_window import ContextWindow

messages = []

for i in range(1, 31):
    messages.append(f"Message {i}")

window = ContextWindow(max_messages=5)

print(window.build(messages))
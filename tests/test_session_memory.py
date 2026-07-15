from app.session.session_memory import SessionMemory

memory = SessionMemory()

memory.add("user", "Hello")
memory.add("assistant", "Hi!")
memory.add("user", "Open Chrome")

for item in memory.history():
    print(item)

print("-" * 40)

memory.clear()

print(memory.history())
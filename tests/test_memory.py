print("Test Started")

from app.memory.memory_manager import MemoryManager

memory = MemoryManager()

print("Current User:", memory.get_user_name())

memory.add_note("Build VishAI Startup")

print("Notes:", memory.get_notes())
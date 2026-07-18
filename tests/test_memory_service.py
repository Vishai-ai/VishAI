from app.memory.memory_service import MemoryService

memory = MemoryService()

memory.remember("Hello VishAI")

print(memory.get_notes())
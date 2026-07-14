from app.memory.memory_manager import MemoryManager

memory = MemoryManager()

memory.set_fact("favorite_car", "BMW")

print(memory.get_fact("favorite_car"))
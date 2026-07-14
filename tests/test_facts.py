from app.memory.memory_manager import MemoryManager

print("===== Memory Fact Test =====")

memory = MemoryManager()

memory.set_fact("favorite_car", "BMW")
memory.set_fact("favorite_language", "Python")

print("Favorite Car:", memory.get_fact("favorite_car"))
print("Favorite Language:", memory.get_fact("favorite_language"))
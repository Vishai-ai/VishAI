from app.memory.memory_engine import MemoryEngine

memory = MemoryEngine()

memory.initialize()

memory.remember(
    "dream_car",
    "Nissan GT-R"
)

memory.remember(
    "project",
    "VishAI"
)

print(memory.recall("dream_car"))

print(memory.recall("project"))

print(memory.health())

memory.shutdown()
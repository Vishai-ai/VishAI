from app.memory.memory_manager import MemoryManager
from app.brain.brain_engine import BrainEngine

memory = MemoryManager()
brain = BrainEngine(memory)

tests = [
    "Please Launch Chrome",
    "Can you Open Calculator",
    "Kindly Run VSCode",
]

for command in tests:
    print(brain.think(command))
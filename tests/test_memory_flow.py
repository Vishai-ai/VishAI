from app.memory.memory_manager import MemoryManager
from app.brain.brain_engine import BrainEngine

memory = MemoryManager()
brain = BrainEngine(memory)

print(brain.think("Remember my favorite car is BMW"))
print(brain.think("What is my favorite car is BMW"))
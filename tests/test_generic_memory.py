from app.brain.brain_engine import BrainEngine
from app.memory.memory_manager import MemoryManager

memory = MemoryManager()
brain = BrainEngine(memory)

print(brain.think("Remember my city is Lucknow"))
print(brain.think("Remember my hobby is Coding"))

print(brain.think("What is my city?"))
print(brain.think("What is my hobby?"))
print(brain.think("What is my favorite subject?"))
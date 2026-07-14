from app.memory.memory_manager import MemoryManager
from app.brain.brain_engine import BrainEngine

memory = MemoryManager()
brain = BrainEngine(memory)

print(brain.think("Open Calculator"))
print(brain.think("Open Notepad"))
print(brain.think("Open Chrome"))
print(brain.think("Open VS Code"))
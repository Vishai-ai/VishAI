from app.brain.brain_engine import BrainEngine

brain = BrainEngine()

brain.initialize()

print(brain.process("What is Python?"))

print("----------------")

print(brain.process("Tell me a joke"))
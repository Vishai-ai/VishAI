from app.brain.brain_engine import BrainEngine


brain = BrainEngine()

print(brain.health())

brain.initialize()

print(brain.health())

print("------------------")

print(brain.process("What is Python?"))

print("------------------")

brain.shutdown()

print(brain.health())
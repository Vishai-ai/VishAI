from app.brain.brain_engine import BrainEngine

brain = BrainEngine()

brain.initialize()

print(
    brain.process(
        "Open Notepad"
    )
)
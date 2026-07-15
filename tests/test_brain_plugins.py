from app.core.container import AppContainer

container = AppContainer()

brain = container.brain

tests = [
    "Open Calculator",
    "Open Chrome",
]

for command in tests:
    print(f"> {command}")
    print(brain.think(command))
    print("-" * 40)
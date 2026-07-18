from app.kernel.engine_registry import EngineRegistry

from app.brain.brain_engine import BrainEngine


registry = EngineRegistry()

brain = BrainEngine()

registry.register(brain)

print(registry.list_engines())

registry.initialize_all()

print(registry.health())

registry.shutdown_all()

print(registry.health())
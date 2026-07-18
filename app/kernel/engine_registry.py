from app.core.base_engine import BaseEngine


class EngineRegistry:
    """
    Registers and manages all VishAI engines.
    """

    def __init__(self):
        self._engines = {}

    def register(self, engine: BaseEngine):

        name = engine.name.lower()

        if name in self._engines:
            raise ValueError(
                f"Engine '{engine.name}' already registered."
            )

        self._engines[name] = engine

    def get(self, name: str):

        return self._engines.get(name.lower())

    def initialize_all(self):

        for engine in self._engines.values():
            engine.initialize()

    def shutdown_all(self):

        for engine in self._engines.values():
            engine.shutdown()

    def health(self):

        report = {}

        for name, engine in self._engines.items():
            report[name] = engine.health()

        return report

    def list_engines(self):

        return list(self._engines.keys())
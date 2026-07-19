from app.core.bootstrap import Bootstrap

boot = Bootstrap()

registry = boot.initialize()

print(registry.all())
from app.core.service_registry import ServiceRegistry

registry = ServiceRegistry()

registry.register("name", "VishAI")

print(registry.get("name"))

print(registry.exists("name"))

registry.remove("name")

print(registry.exists("name"))
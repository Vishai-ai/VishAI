from app.core.application import VishAIApplication

app = VishAIApplication()

registry = app.initialize()

print(registry.exists("ai"))

print(registry.exists("memory"))

print(registry.exists("knowledge"))

print(registry.exists("planner"))

print(registry.exists("executor"))
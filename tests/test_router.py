from app.router.router_engine import RouterEngine
from app.brain.intent import Intent

router = RouterEngine()

print(router.route(Intent.AI_CHAT))
print(router.route(Intent.MEMORY))
print(router.route(Intent.AUTOMATION))
print(router.route(Intent.CODING))
print(router.route(Intent.SEARCH))
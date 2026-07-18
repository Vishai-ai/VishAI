from app.router.command_router import CommandRouter
from app.brain.intent import Intent

router = CommandRouter()

print(router.route(Intent.AI_CHAT))
print(router.route(Intent.AUTOMATION))
print(router.route(Intent.MEMORY))
print(router.route(Intent.SEARCH))
print(router.route(Intent.CODING))
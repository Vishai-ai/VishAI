from app.router.command_router import CommandRouter

router = CommandRouter()

print(router.route("memory_save"))
print(router.route("memory_recall"))
print(router.route("automation"))
print(router.route("knowledge"))
print(router.route("xyz"))
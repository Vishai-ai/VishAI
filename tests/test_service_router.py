from app.core.container import AppContainer
from app.router.service_router import ServiceRouter

container = AppContainer()

router = ServiceRouter(container.plugins)

print(router.route("memory", ""))
print(router.route("automation", "Open Calculator"))
class ServiceRouter:
    """Routes requests to the correct VishAI service."""

    def __init__(self, plugin_manager):
        self.plugins = plugin_manager

    def route(self, service: str, command: str):

        plugin = self.plugins.get_plugin(service)

        if plugin:
            return plugin.execute(command)

        return f"Service '{service}' not found."
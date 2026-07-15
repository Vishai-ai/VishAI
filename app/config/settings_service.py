from app.config.config_manager import ConfigManager


class SettingsService:
    """Manage VishAI runtime settings."""

    def __init__(self):
        self.config = ConfigManager()

    def get(self, key: str):
        return self.config.settings.get(key)

    def set(self, key: str, value):
        self.config.settings[key] = value
        self.config.save()

    def all(self):
        return self.config.settings
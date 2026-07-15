from app.config.settings_service import SettingsService

settings = SettingsService()

print(settings.all())

settings.set("assistant_name", "VishAI")

print(settings.get("assistant_name"))

from app.desktop.desktop_service import DesktopService


desktop = DesktopService()

success, message = desktop.open_application("notepad")

print(success)

print(message)
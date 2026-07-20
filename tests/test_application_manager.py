from app.desktop.application_manager import ApplicationManager

app = ApplicationManager()

print(app.exists("chrome"))

print(app.category("chrome"))

print(app.search("please open chrome"))

print(app.open("chrome"))
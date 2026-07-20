from app.file_system.file_manager import FileManager

fm = FileManager()

print(fm.create_folder("DemoFolder"))

print(fm.exists("DemoFolder"))
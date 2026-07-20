import subprocess

from app.automation.app_registry import AppRegistry


class ApplicationManager:
    """
    Handles launching registered desktop applications.
    """

    def __init__(self):

        self.registry = AppRegistry()

    # ==========================================
    # Open Application
    # ==========================================

    def open(self, app_name: str):

        app_name = app_name.lower().strip()

        executable = self.registry.get(app_name)

        if executable is None:

            return False, f"{app_name} is not registered."

        try:

            subprocess.Popen(executable)

            return True, f"{app_name.title()} opened successfully."

        except FileNotFoundError:

            return False, f"Executable not found:\n{executable}"

        except Exception as e:

            return False, str(e)

    # ==========================================
    # Exists
    # ==========================================

    def exists(self, app_name: str):

        return self.registry.exists(app_name)

    # ==========================================
    # Category
    # ==========================================

    def category(self, app_name: str):

        return self.registry.category(app_name)

    # ==========================================
    # Search
    # ==========================================

    def search(self, text: str):

        return self.registry.search(text)
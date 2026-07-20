import subprocess

from app.desktop.app_registry import AppRegistry


class ApplicationManager:

    """
    Responsible only for
    opening desktop applications.
    """

    def __init__(self):

        self.registry = AppRegistry()

    def open(self, app_name: str):

        executable = self.registry.get(app_name)

        if executable is None:

            return False, f"{app_name} is not registered."

        try:

            subprocess.Popen(executable)

            return True, f"{app_name.title()} opened successfully."

        except Exception as e:

            return False, str(e)

    def exists(self, app_name):

        return self.registry.exists(app_name)
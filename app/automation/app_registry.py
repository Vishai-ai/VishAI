from pathlib import Path


class AppRegistry:
    """
    Stores all applications known by VishAI.
    """

    def __init__(self):

        self.apps = {

            "notepad": "notepad.exe",

            "calculator": "calc.exe",

            "paint": "mspaint.exe",

            "cmd": "cmd.exe",

            "explorer": "explorer.exe",

            "powershell": "powershell.exe",

        }

    def get(self, name: str):

        return self.apps.get(name.lower())

    def register(self, name: str, executable: str):

        self.apps[name.lower()] = executable

    def exists(self, name: str):

        return name.lower() in self.apps

    def all_apps(self):

        return self.apps
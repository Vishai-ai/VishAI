import os


class AppRegistry:
    """
    Stores executable paths of supported applications.
    """

    def __init__(self):

        self.apps = {

            "notepad": "notepad.exe",

            "calculator": "calc.exe",

            "paint": "mspaint.exe",

            "cmd": "cmd.exe",

            "explorer": "explorer.exe",

            "wordpad": "write.exe",

            "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",

            "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",

            "vscode": r"C:\Users\Admin\AppData\Local\Programs\Microsoft VS Code\Code.exe"

        }

    def get(self, app_name):

        return self.apps.get(app_name.lower())

    def exists(self, app_name):

        return app_name.lower() in self.apps
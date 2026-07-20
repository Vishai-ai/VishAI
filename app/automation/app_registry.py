class AppRegistry:
    """
    Central registry for all applications supported by VishAI.
    """

    def __init__(self):

        self.apps = {

            "notepad": "notepad.exe",

            "calculator": "calc.exe",
            "calc": "calc.exe",

            "paint": "mspaint.exe",

            "cmd": "cmd.exe",
            "command prompt": "cmd.exe",

            "powershell": "powershell.exe",

            "explorer": "explorer.exe",

            "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",

            "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",

            "vscode": r"C:\Users\Admin\AppData\Local\Programs\Microsoft VS Code\Code.exe",
            "visual studio code": r"C:\Users\Admin\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        }

    def get(self, name: str):

        return self.apps.get(name.lower().strip())

    def register(self, name: str, executable: str):

        self.apps[name.lower()] = executable

    def exists(self, name: str):

        return name.lower().strip() in self.apps

    def all_apps(self):

        return self.apps

    def search(self, text: str):

        text = text.lower()

        for app in self.apps:

            if app in text:

                return app

        return None
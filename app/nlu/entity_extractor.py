class EntityExtractor:
    """
    Extracts entities like application names from text.
    """

    def __init__(self):

        self.app_aliases = {

            "chrome": "chrome",

            "google chrome": "chrome",

            "calculator": "calculator",

            "calc": "calculator",

            "paint": "paint",

            "notepad": "notepad",

            "command prompt": "cmd",

            "cmd": "cmd",

            "powershell": "powershell",

            "explorer": "explorer",

            "visual studio code": "vscode",

            "vs code": "vscode",

            "vscode": "vscode",

        }

    def extract_application(self, text: str):

        text = text.lower()

        for alias, app in self.app_aliases.items():

            if alias in text:

                return app

        return None
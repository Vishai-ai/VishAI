from pathlib import Path


class AppRegistry:
    """
    Central registry for all applications supported by VishAI.

    Responsibilities
    ----------------
    - Store all known applications
    - Return executable path
    - Search applications inside text
    - Categorize applications
    """

    def __init__(self):

        self.apps = {

            # ==========================================
            # Desktop Applications
            # ==========================================

            "desktop": {

                "notepad": "notepad.exe",

                "calculator": "calc.exe",
                "calc": "calc.exe",

                "paint": "mspaint.exe",

                "cmd": "cmd.exe",
                "command prompt": "cmd.exe",

                "powershell": "powershell.exe",

                "explorer": "explorer.exe",

                "vscode": r"C:\Users\Admin\AppData\Local\Programs\Microsoft VS Code\Code.exe",

                "visual studio code": r"C:\Users\Admin\AppData\Local\Programs\Microsoft VS Code\Code.exe",

            },

            # ==========================================
            # Browsers
            # ==========================================

            "browser": {

                "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",

                "google chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",

                "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",

                "microsoft edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",

            }

        }

    # ===================================================
    # Get executable
    # ===================================================

    def get(self, name: str):

        name = name.lower().strip()

        for category in self.apps.values():

            if name in category:

                return category[name]

        return None

    # ===================================================
    # Get category
    # ===================================================

    def category(self, name: str):

        name = name.lower().strip()

        for category_name, category in self.apps.items():

            if name in category:

                return category_name

        return None

    # ===================================================
    # Register new application
    # ===================================================

    def register(

        self,

        category: str,

        name: str,

        executable: str

    ):

        category = category.lower().strip()

        name = name.lower().strip()

        if category not in self.apps:

            self.apps[category] = {}

        self.apps[category][name] = executable

    # ===================================================
    # Exists
    # ===================================================

    def exists(self, name: str):

        return self.get(name) is not None

    # ===================================================
    # Search inside text
    # ===================================================

    def search(self, text: str):

        text = text.lower()

        for category in self.apps.values():

            for app in category:

                if app in text:

                    return app

        return None

    # ===================================================
    # Return all applications
    # ===================================================

    def all_apps(self):

        return self.apps

    # ===================================================
    # Return one category
    # ===================================================

    def all_in_category(self, category: str):

        category = category.lower().strip()

        return self.apps.get(category, {})
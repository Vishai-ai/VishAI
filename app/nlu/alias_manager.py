class AliasManager:
    """Converts alternative words into standard VishAI commands."""

    def __init__(self):
        self.aliases = {
            "launch": "open",
            "start": "open",
            "run": "open",
            "browser": "chrome",
            "google chrome": "chrome",
            "visual studio code": "vs code",
            "vscode": "vs code",
        }

    def normalize(self, text: str) -> str:
        text = text.lower()

        for alias, original in self.aliases.items():
            text = text.replace(alias, original)

        return " ".join(text.split())
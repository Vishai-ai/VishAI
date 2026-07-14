class CommandAnalyzer:
    """Analyzes automation commands."""

    APPS = {
        "calculator": "calculator",
        "notepad": "notepad",
        "chrome": "chrome",
        "vs code": "vscode",
    }

    def analyze(self, command: str):
        command = command.lower().strip()

        if command.startswith("open "):
            target = command[5:].strip()

            if "." in target:
                return ("website", target)

            if target in self.APPS:
                return ("app", self.APPS[target])

        return ("unknown", None)
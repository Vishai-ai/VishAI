from pathlib import Path


class ProjectAnalyzer:
    """
    Analyzes the VishAI project structure.
    """

    def __init__(self, root="."):

        self.root = Path(root)

    def analyze(self):

        report = {
            "python_files": 0,
            "folders": 0,
            "tests": 0,
            "modules": []
        }

        # Count folders
        for folder in self.root.rglob("*"):

            if folder.is_dir():
                report["folders"] += 1

        # Analyze python files
        for file in self.root.rglob("*.py"):

            report["python_files"] += 1

            if "tests" in file.parts:
                report["tests"] += 1

            report["modules"].append(file.stem)

        report["modules"].sort()

        return report
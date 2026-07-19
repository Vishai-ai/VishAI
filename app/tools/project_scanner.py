from pathlib import Path


class ProjectScanner:
    """
    Scans the VishAI project structure.
    """

    def __init__(self, root="."):

        self.root = Path(root)

    def scan_python_files(self):

        files = []

        for file in self.root.rglob("*.py"):

            files.append(str(file))

        return sorted(files)

    def count_python_files(self):

        return len(self.scan_python_files())
import platform
import subprocess
from pathlib import Path


def separator():
    print("=" * 60)


separator()
print("VishAI Developer Dashboard")
separator()

print(f"Python Version : {platform.python_version()}")
print(f"Operating System : {platform.system()} {platform.release()}")

separator()

print("Project Structure")

folders = [
    "app",
    "tests",
    "config",
    "data",
]

for folder in folders:
    exists = Path(folder).exists()
    status = "OK" if exists else "MISSING"
    print(f"{folder:<15} {status}")

separator()

print("Git Status")

try:
    subprocess.run(["git", "status", "--short"])
except Exception:
    print("Git not available.")

separator()

print("Dashboard Finished")
separator()
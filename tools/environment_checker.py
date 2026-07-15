import platform
import shutil
import sys
from pathlib import Path

try:
    import psutil
except ImportError:
    psutil = None


def check_program(name):
    return shutil.which(name) is not None


def print_result(name, status):
    icon = "✅" if status else "❌"
    print(f"{icon} {name}")


print("=" * 60)
print("VishAI Environment Checker")
print("=" * 60)

print(f"Python : {platform.python_version()}")
print(f"OS     : {platform.system()} {platform.release()}")
print()

print_result("Git", check_program("git"))
print_result("Python", check_program("python"))
print_result("FFmpeg", check_program("ffmpeg"))
print_result("Ollama", check_program("ollama"))

print()

if psutil:
    ram = round(psutil.virtual_memory().total / (1024**3), 2)
    cpu = psutil.cpu_count(logical=True)

    print(f"CPU Threads : {cpu}")
    print(f"RAM         : {ram} GB")

print()

folders = [
    "app",
    "config",
    "data",
    "docs",
    "tests",
    "tools",
]

print("Project Folders")

for folder in folders:
    print_result(folder, Path(folder).exists())

print()

print("Environment Check Complete")
print("=" * 60)
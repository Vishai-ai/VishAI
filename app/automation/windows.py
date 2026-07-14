import subprocess

from app.core.logger import logger
from app.config.config_manager import ConfigManager

class WindowsAutomation:
    """Handles Windows automation."""
    
    def __init__(self):
        self.config = ConfigManager()



    def open_app(self, executable: str):
        """Open any application using its executable."""

        try:
             subprocess.Popen(executable)

             return f"Opening {executable}"

        except Exception as e:
             return f"Failed to open {executable}: {e}"
    
    def open_calculator(self):
        """Open Windows Calculator."""

        try:
            subprocess.Popen("calc.exe")
            logger.info("Calculator opened successfully.")
            return "Opening Calculator..."

        except Exception as e:
            logger.error(f"Failed to open Calculator: {e}")
            return "Failed to open Calculator."
        
    def open_notepad(self):
        """Open Windows Notepad."""

        try:
            subprocess.Popen("notepad.exe")
            logger.info("Notepad opened successfully.")
            return "Opening Notepad..."

        except Exception as e:
            logger.error(f"Failed to open Notepad: {e}")
            return "Failed to open Notepad."
        
    def open_chrome(self):
        """Open Google Chrome."""

        try:
             chrome = self.config.get("chrome_path")

             subprocess.Popen(chrome)

             logger.info("Chrome opened successfully.")
             return "Opening Chrome..."

        except Exception as e:
             logger.error(f"Failed to open Chrome: {e}")
             return "Failed to open Chrome."
    def open_vscode(self):
        """Open Visual Studio Code."""

        try:
            vscode = self.config.get("vscode_path")

            subprocess.Popen(vscode)

            logger.info("VS Code opened successfully.")
            return "Opening VS Code..."

        except Exception as e:
            logger.error(f"Failed to open VS Code: {e}")
            return "Failed to open VS Code."
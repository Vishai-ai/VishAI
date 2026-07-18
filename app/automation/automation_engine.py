import subprocess
import time

import pyautogui
import pyperclip

from app.core.base_engine import BaseEngine


class AutomationEngine(BaseEngine):
    """
    VishAI Automation Engine

    Controls:
    - Applications
    - Keyboard
    - Mouse
    - Clipboard
    - Screenshots
    """

    def __init__(self):
        super().__init__("Automation")

    # -------------------------------------------------
    # Engine Lifecycle
    # -------------------------------------------------

    def initialize(self) -> bool:
        self.initialized = True

        # Move mouse to top-left corner to stop automation
        pyautogui.FAILSAFE = True

        # Small delay after every action
        pyautogui.PAUSE = 0.2

        return True

    def shutdown(self):
        self.initialized = False

    def health(self):
        return {
            "engine": self.name,
            "initialized": self.initialized
        }

    # -------------------------------------------------
    # Timing
    # -------------------------------------------------

    def wait(self, seconds: float):
        """Pause execution."""
        time.sleep(seconds)

    # -------------------------------------------------
    # Applications
    # -------------------------------------------------

    def open_application(self, command: str):
        """Open any application using its executable."""
        subprocess.Popen(command)

    def open_notepad(self):
        subprocess.Popen("notepad.exe")

    def open_calculator(self):
        subprocess.Popen("calc.exe")

    def open_cmd(self):
        subprocess.Popen("cmd.exe")

    def open_paint(self):
        subprocess.Popen("mspaint.exe")

    # -------------------------------------------------
    # Keyboard
    # -------------------------------------------------

    def type_text(self, text: str):
        """
        Paste text quickly using clipboard.
        """
        pyperclip.copy(text)
        pyautogui.hotkey("ctrl", "v")

    def press(self, key: str):
        pyautogui.press(key)

    def hotkey(self, *keys):
        pyautogui.hotkey(*keys)

    def write(self, text: str):
        pyautogui.write(text)

    # -------------------------------------------------
    # Mouse
    # -------------------------------------------------

    def move(self, x: int, y: int):
        pyautogui.moveTo(x, y, duration=0.3)

    def click(self):
        pyautogui.click()

    def double_click(self):
        pyautogui.doubleClick()

    def right_click(self):
        pyautogui.rightClick()

    def scroll(self, amount: int):
        pyautogui.scroll(amount)

    # -------------------------------------------------
    # Screenshots
    # -------------------------------------------------

    def screenshot(self, filename="screenshot.png"):
        pyautogui.screenshot(filename)
        return filename

    # -------------------------------------------------
    # Screen Information
    # -------------------------------------------------

    def screen_size(self):
        return pyautogui.size()

    def mouse_position(self):
        return pyautogui.position()
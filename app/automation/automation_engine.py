import subprocess
import time

import pyautogui
import pyperclip

from app.core.base_engine import BaseEngine


class AutomationEngine(BaseEngine):
    """
    VishAI Automation Engine

    Handles:
    - Desktop Automation
    - Keyboard
    - Mouse
    - Clipboard
    - Screenshots
    """

    def __init__(self):

        super().__init__("Automation")

        self.initialized = False

    # =====================================================
    # Lifecycle
    # =====================================================

    def initialize(self):

        if self.initialized:
            return True

        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.2

        self.initialized = True

        return True

    def shutdown(self):

        self.initialized = False

    def health(self):

        return {

            "engine": self.name,

            "initialized": self.initialized

        }

    # =====================================================
    # Timing
    # =====================================================

    def wait(self, seconds: float):

        time.sleep(seconds)

    # =====================================================
    # Applications
    # =====================================================

    def open_application(self, executable: str):

        subprocess.Popen(executable)

    def open_notepad(self):

        subprocess.Popen("notepad.exe")

    def open_calculator(self):

        subprocess.Popen("calc.exe")

    def open_cmd(self):

        subprocess.Popen("cmd.exe")

    def open_paint(self):

        subprocess.Popen("mspaint.exe")

    # =====================================================
    # Keyboard
    # =====================================================

    def type_text(self, text: str):
        """
        Types text into the currently focused window.
        """

        pyautogui.write(

            text,

            interval=0.02

        )

    def paste_text(self, text: str):
        """
        Pastes text using clipboard.
        """

        pyperclip.copy(text)

        pyautogui.hotkey(

            "ctrl",

            "v"

        )

    def press(self, key: str):

        pyautogui.press(key)

    def hotkey(self, *keys):

        pyautogui.hotkey(*keys)

    def write(self, text: str):

        pyautogui.write(

            text,

            interval=0.02

        )

    # =====================================================
    # Mouse
    # =====================================================

    def move(self, x: int, y: int):

        pyautogui.moveTo(

            x,

            y,

            duration=0.3

        )

    def click(self):

        pyautogui.click()

    def double_click(self):

        pyautogui.doubleClick()

    def right_click(self):

        pyautogui.rightClick()

    def scroll(self, amount: int):

        pyautogui.scroll(amount)

    # =====================================================
    # Screen
    # =====================================================

    def screenshot(

        self,

        filename="screenshot.png"

    ):

        pyautogui.screenshot(filename)

        return filename

    def screen_size(self):

        return pyautogui.size()

    def mouse_position(self):

        return pyautogui.position()
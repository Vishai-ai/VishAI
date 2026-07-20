from app.desktop.desktop_service import DesktopService


class CommandExecutor:
    """
    Executes automation commands.

    This class should NEVER know how applications
    are opened. It delegates everything to DesktopService.
    """

    def __init__(self):

        self.desktop = DesktopService()

    def execute(self, command: str):

        if not command:

            return "Empty command."

        success, message = self.desktop.execute(command)

        return message
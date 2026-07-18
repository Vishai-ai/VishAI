from app.automation.action import Action


class ActionParser:
    """
    Converts natural language into structured actions.
    """

    def parse(self, command: str) -> Action:

        text = command.lower()

        if "notepad" in text:
            return Action(
                action="open_app",
                target="notepad"
            )

        if "calculator" in text:
            return Action(
                action="open_app",
                target="calculator"
            )

        if "paint" in text:
            return Action(
                action="open_app",
                target="paint"
            )

        if "cmd" in text:
            return Action(
                action="open_app",
                target="cmd"
            )

        return Action(
            action="chat",
            value=command
        )
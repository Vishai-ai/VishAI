import re


class InputProcessor:
    """
    Cleans and normalizes user input before processing.
    """

    def process(self, text: str) -> str:

        if not text:
            return ""

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text)

        # Trim
        text = text.strip()

        return text
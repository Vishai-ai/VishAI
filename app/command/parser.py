class CommandParser:
    """Extracts key-value data from commands."""

    def parse_memory(self, text: str):

        text = text.lower()

        if "favorite car is" in text:
            value = text.split("favorite car is")[1].strip()
            return "favorite_car", value

        if "favorite language is" in text:
            value = text.split("favorite language is")[1].strip()
            return "favorite_language", value

        return None, None
class CommandParser:
    """Extracts key-value data from commands."""

    def parse_memory(self, text: str):
        """Parse generic 'Remember my ... is ...' commands."""

        original_text = text.strip()
        lower_text = original_text.lower()

        if not lower_text.startswith("remember my "):
            return None, None

        content = original_text[len("Remember my "):]

        if " is " not in content:
            return None, None

        key, value = content.split(" is ", 1)

        key = key.strip().lower().replace(" ", "_")
        value = value.strip()

        return key, value
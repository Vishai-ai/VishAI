class TextNormalizer:
    """Normalizes user input."""

    def normalize(self, text: str) -> str:
        text = text.lower().strip()

        polite_words = [
            "please",
            "can you",
            "could you",
            "would you",
            "kindly",
        ]

        for word in polite_words:
            text = text.replace(word, "")

        return " ".join(text.split())
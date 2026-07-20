class TextNormalizer:
    """
    Normalizes user text before intent detection.
    """

    def normalize(self, text: str):

        text = text.lower()

        text = text.replace("please", "")

        text = text.replace("could you", "")

        text = text.replace("can you", "")

        text = text.replace("kindly", "")

        text = text.replace("google", "")

        text = " ".join(text.split())

        return text.strip()
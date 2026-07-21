from app.nlu.text_normalizer import TextNormalizer
from app.nlu.entity_extractor import EntityExtractor


class CommandParser:
    """
    Converts natural language into a structured command.
    """

    def __init__(self):

        self.normalizer = TextNormalizer()
        self.extractor = EntityExtractor()

    def parse(self, text: str):

        text = self.normalizer.normalize(text)

        app = self.extractor.extract_application(text)

        action = None

        if any(word in text for word in [
            "open",
            "launch",
            "start",
            "run",
            "execute"
        ]):

            action = "open_app"

        return {

            "action": action,

            "target": app,

            "text": text

        }
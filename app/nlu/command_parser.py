from app.nlu.text_normalizer import TextNormalizer
from app.nlu.entity_extractor import EntityExtractor


class CommandParser:
    """
    Converts natural language into structured commands.
    """

    def __init__(self):

        self.normalizer = TextNormalizer()

        self.extractor = EntityExtractor()

    def parse(self, text: str):

        text = self.normalizer.normalize(text)

        application = self.extractor.extract_application(text)

        action = None

        if any(word in text for word in [

            "open",

            "launch",

            "start",

            "run",

            "execute"

        ]):

            action = "OPEN"

        return {

            "action": action,

            "application": application,

            "text": text

        }
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

        original_text = text

        text = self.normalizer.normalize(text).lower().strip()

        app = self.extractor.extract_application(text)

        action = None
        target = app
        value = None

        # ==================================================
        # Google Search
        # ==================================================

        if text.startswith("search "):

            action = "search"

            value = text.replace("search", "", 1).strip()

            target = "google"

        # ==================================================
        # YouTube Search
        # ==================================================

        elif text.startswith("youtube "):

            action = "youtube_search"

            value = text.replace("youtube", "", 1).strip()

            target = "youtube"

        elif text.startswith("search on youtube "):

            action = "youtube_search"

            value = text.replace("search on youtube", "", 1).strip()

            target = "youtube"

        # ==================================================
        # Open Applications / Websites
        # ==================================================

        elif any(word in text for word in [

            "open",

            "launch",

            "start",

            "run",

            "execute"

        ]):

            action = "open_app"

        # ==================================================
        # Return Parsed Command
        # ==================================================

        return {

            "action": action,

            "target": target,

            "value": value,

            "text": text,

            "original_text": original_text

        }
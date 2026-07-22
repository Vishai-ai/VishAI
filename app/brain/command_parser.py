from app.nlu.text_normalizer import TextNormalizer
from app.nlu.entity_extractor import EntityExtractor
print(">>> BRAIN COMMAND PARSER LOADED <<<")
class CommandParser:

    def __init__(self):

        self.normalizer = TextNormalizer()
        self.extractor = EntityExtractor()

    def parse(self, text: str):

        original = text

        print("RAW :", text)

        text = self.normalizer.normalize(text)

        print("NORMALIZED :", text)

        text = text.lower().strip()

        print("LOWER :", text)

        action = None
        target = None
        value = None

        # -----------------------------
        # Open App + Type Text
        # -----------------------------

        if " and type " in text:

            before, after = text.split(" and type ", 1)

            words = before.split()

            if len(words) >= 2:

                action = "open_and_type"

                target = words[-1]

                value = after.strip()

        # -----------------------------
        # Google Search
        # -----------------------------

        elif text.startswith("search "):

            action = "search"

            target = "google"

            value = text.replace("search", "", 1).strip()

        # -----------------------------
        # YouTube Search
        # -----------------------------

        elif text.startswith("youtube "):

            action = "youtube_search"

            target = "youtube"

            value = text.replace("youtube", "", 1).strip()

        elif text.startswith("search on youtube "):

            action = "youtube_search"

            target = "youtube"

            value = text.replace(
                "search on youtube",
                "",
                1
            ).strip()

        # -----------------------------
        # Open Website
        # -----------------------------

        elif text.startswith("open "):

            site = text.replace(
                "open",
                "",
                1
            ).strip()

            app = self.extractor.extract_application(text)

            if app:

                action = "open_app"

                target = app

            else:

                action = "open_site"

                target = site

        # -----------------------------

        return {

            "action": action,

            "target": target,

            "value": value,

            "text": text,

            "original_text": original

        }
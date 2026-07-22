from app.brain.parsed_command import ParsedCommand
from app.brain.command_step import CommandStep

from app.nlu.text_normalizer import TextNormalizer
from app.nlu.entity_extractor import EntityExtractor


class CommandParserV2:
    """
    Multi-step command parser.
    """

    def __init__(self):

        self.normalizer = TextNormalizer()

        self.extractor = EntityExtractor()

    def parse(self, text: str):

        original = text

        text = self.normalizer.normalize(text)

        text = text.lower().strip()

        parsed = ParsedCommand(original)

        # -----------------------------
        # Split using AND
        # -----------------------------

        commands = [

            part.strip()

            for part in text.split(" and ")

        ]

        for command in commands:

            self._parse_single(

                command,

                parsed

            )

        return parsed

    # --------------------------------

    def _parse_single(

        self,

        text,

        parsed

    ):

        # -------------------------
        # Search
        # -------------------------

        if text.startswith("search "):

            parsed.add_step(

                CommandStep(

                    action="browser_search",

                    target="google",

                    value=text.replace(

                        "search",

                        "",

                        1

                    ).strip()

                )

            )

            return

        # -------------------------
        # YouTube
        # -------------------------

        if text.startswith("youtube "):

            parsed.add_step(

                CommandStep(

                    action="browser_search",

                    target="youtube",

                    value=text.replace(

                        "youtube",

                        "",

                        1

                    ).strip()

                )

            )

            return

        # -------------------------
        # Open
        # -------------------------

        if text.startswith("open "):

            target = text.replace(

                "open",

                "",

                1

            ).strip()

            app = self.extractor.extract_application(

                text

            )

            if app:

                parsed.add_step(

                    CommandStep(

                        action="open_app",

                        target=app

                    )

                )

            else:

                parsed.add_step(

                    CommandStep(

                        action="open_site",

                        target=target

                    )

                )

            return

        # -------------------------
        # Type
        # -------------------------

        if text.startswith("type "):

            parsed.add_step(

                CommandStep(

                    action="type",

                    value=text.replace(

                        "type",

                        "",

                        1

                    ).strip()

                )

            )

            return
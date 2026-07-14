from app.nlu.normalizer import TextNormalizer
from app.nlu.alias_manager import AliasManager


class NLUPipeline:
    """Processes raw user text before intent detection."""

    def __init__(self):
        self.normalizer = TextNormalizer()
        self.alias_manager = AliasManager()

    def process(self, text: str) -> str:
        text = self.normalizer.normalize(text)
        text = self.alias_manager.normalize(text)
        return text
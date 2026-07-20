from app.nlu.intent_classifier import IntentClassifier
from app.nlu.entity_extractor import EntityExtractor


class NLUEngine:

    def __init__(self):

        self.intent = IntentClassifier()

        self.entities = EntityExtractor()
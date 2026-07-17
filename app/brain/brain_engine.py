from app.brain.intent_detector import IntentDetector
from app.brain.task_dispatcher import TaskDispatcher


class BrainEngine:
    """Main Brain of VishAI"""

    def __init__(self):
        self.intent_detector = IntentDetector()
        self.dispatcher = TaskDispatcher()

    def process(self, prompt: str):

        intent = self.intent_detector.detect(prompt)

        return self.dispatcher.dispatch(
            intent=intent,
            prompt=prompt,
        )
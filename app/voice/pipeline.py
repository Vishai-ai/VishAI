class VoicePipeline:
    """Coordinates the complete voice processing pipeline."""

    def __init__(self, wake_word, speech_to_text, text_to_speech):
        self.wake_word = wake_word
        self.speech_to_text = speech_to_text
        self.text_to_speech = text_to_speech

    def status(self):
        return {
            "wake_word": "ready",
            "speech_to_text": "ready",
            "text_to_speech": "ready",
        }
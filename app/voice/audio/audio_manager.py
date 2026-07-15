class AudioManager:
    """Handles microphone and speaker devices."""

    def __init__(self):
        self.microphone = None
        self.speaker = None

    def status(self):
        return {
            "microphone": "not initialized",
            "speaker": "not initialized",
        }
class VoiceManager:
    """Base class for future voice support."""

    def __init__(self):
        self.enabled = False

    def enable(self):
        self.enabled = True
        return "Voice Enabled"

    def disable(self):
        self.enabled = False
        return "Voice Disabled"

    def status(self):
        return "Enabled" if self.enabled else "Disabled"
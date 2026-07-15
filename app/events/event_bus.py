class EventBus:
    """Simple publish-subscribe event system."""

    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_name, callback):
        self.listeners.setdefault(event_name, []).append(callback)

    def publish(self, event_name, data=None):
        for callback in self.listeners.get(event_name, []):
            callback(data)
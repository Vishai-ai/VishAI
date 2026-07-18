from collections import defaultdict


class EventBus:
    """
    Central communication hub for VishAI.

    Modules publish events.
    Other modules subscribe to events.

    This keeps modules independent.
    """

    def __init__(self):

        self.listeners = defaultdict(list)

    def subscribe(self, event_name: str, callback):

        self.listeners[event_name].append(callback)

    def publish(self, event_name: str, data=None):

        if event_name not in self.listeners:
            return

        for callback in self.listeners[event_name]:

            callback(data)
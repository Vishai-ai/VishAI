from app.events.event_bus import EventBus

bus = EventBus()


def logger(data):
    print(f"LOG: {data}")


def dashboard(data):
    print(f"DASHBOARD: {data}")


bus.subscribe("app_opened", logger)
bus.subscribe("app_opened", dashboard)

bus.publish("app_opened", "Calculator")
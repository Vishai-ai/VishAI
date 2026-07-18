from app.events.event_bus import EventBus


bus = EventBus()


def memory_listener(data):

    print("Memory received:", data)


def planner_listener(data):

    print("Planner received:", data)


bus.subscribe("user_message", memory_listener)

bus.subscribe("user_message", planner_listener)

bus.publish(

    "user_message",

    "Hello VishAI"

)
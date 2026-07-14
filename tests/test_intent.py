from app.brain.intent_detector import IntentDetector

detector = IntentDetector()

tests = [
    "Remember my city is Delhi",
    "What is my city?",
    "Open Calculator",
    "Search Google",
    "Create Task Buy Milk",
    "Learn Python",
    "Hello VishAI",
]

for text in tests:
    print(f"{text} -> {detector.detect(text)}")
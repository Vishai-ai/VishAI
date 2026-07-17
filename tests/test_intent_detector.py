from app.brain.intent_detector import IntentDetector

detector = IntentDetector()

print(detector.detect("Open Chrome"))
print(detector.detect("Remember my name"))
print(detector.detect("Write Python code"))
print(detector.detect("Search YouTube"))
print(detector.detect("Who is Elon Musk?"))
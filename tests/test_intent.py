from app.brain.intent_detector import IntentDetector

detector = IntentDetector()

print(detector.detect("Open Chrome"))
print(detector.detect("Remember my name"))
print(detector.detect("Python error"))
print(detector.detect("Who is Elon Musk?"))
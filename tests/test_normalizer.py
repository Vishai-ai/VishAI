from app.nlu.normalizer import TextNormalizer

normalizer = TextNormalizer()

tests = [
    "Please Open Calculator",
    "Can you Open Chrome",
    "Could you open VS Code",
    "Kindly Open Notepad",
]

for test in tests:
    print(normalizer.normalize(test))
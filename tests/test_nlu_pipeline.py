from app.nlu.pipeline import NLUPipeline

pipeline = NLUPipeline()

tests = [
    "Please Launch Chrome",
    "Can you Start Calculator",
    "Kindly Run VSCode",
    "Could you Open Browser",
]

for command in tests:
    print(command)
    print(" -> ", pipeline.process(command))
    print("-" * 40)
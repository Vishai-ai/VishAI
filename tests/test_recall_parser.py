from app.command.parser import CommandParser

parser = CommandParser()

tests = [
    "What is my city?",
    "What is my hobby?",
    "What is my favorite subject?",
]

for command in tests:
    key = parser.parse_recall(command)
    print(key)
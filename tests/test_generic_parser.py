from app.command.parser import CommandParser

parser = CommandParser()

tests = [
    "Remember my city is Lucknow",
    "Remember my hobby is Coding",
    "Remember my dream is Build VishAI",
    "Remember my favorite subject is Physics",
]

for command in tests:
    key, value = parser.parse_memory(command)
    print(f"{key} -> {value}")
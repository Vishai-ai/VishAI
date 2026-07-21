from app.brain.command_parser import CommandParser

parser = CommandParser()

result = parser.parse("open notepad")

print(result)
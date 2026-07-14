from app.command.parser import CommandParser

parser = CommandParser()

key, value = parser.parse_memory(
    "Remember my favorite car is BMW"
)

print(key)
print(value)
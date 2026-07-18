from app.automation.action_parser import ActionParser

parser = ActionParser()

commands = [
    "Open Notepad",
    "Launch Calculator",
    "Open Paint",
    "Run CMD",
    "Who are you?"
]

for cmd in commands:

    action = parser.parse(cmd)

    print("----------------")

    print(cmd)

    print(action)
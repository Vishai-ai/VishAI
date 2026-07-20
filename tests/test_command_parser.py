from app.brain.command_parser import CommandParser

parser = CommandParser()

commands = [

    "open chrome",

    "launch vscode",

    "start calculator",

    "run paint",

    "please open visual studio code"

]

for command in commands:

    print(parser.parse(command))
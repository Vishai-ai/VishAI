from app.command.input_processor import InputProcessor

processor = InputProcessor()

commands = [

    "   Open     Chrome   ",

    " Launch     Calculator ",

    "",

    "   Hello VishAI   "

]

for command in commands:

    print(processor.process(command))
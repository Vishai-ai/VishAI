from app.automation.command_executor import CommandExecutor

executor = CommandExecutor()

commands = [

    "Open Notepad",

    "Launch Notepad",

    "Start Calculator",

    "Open Paint",

    "Run CMD",

]

for command in commands:

    print(command)

    print(executor.execute(command))

    print("-" * 30)
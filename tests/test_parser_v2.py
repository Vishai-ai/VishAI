from app.brain.parser_v2 import CommandParserV2

parser = CommandParserV2()

parsed = parser.parse(

    "open chrome and search python tutorial"

)

print()

for step in parsed.steps:

    print(step)
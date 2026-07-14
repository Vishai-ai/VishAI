from app.nlu.alias_manager import AliasManager

alias = AliasManager()

tests = [
    "Launch Chrome",
    "Start Chrome",
    "Run Chrome",
    "Open Browser",
    "Launch Visual Studio Code",
    "Run VSCode",
]

for test in tests:
    print(f"{test} -> {alias.normalize(test)}")
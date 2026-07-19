from app.tools.project_analyzer import ProjectAnalyzer

analyzer = ProjectAnalyzer()

report = analyzer.analyze()

print()

print("Folders :", report["folders"])

print("Python Files :", report["python_files"])

print("Tests :", report["tests"])

print()

print("Modules")

print("----------------------")

for module in report["modules"]:

    print(module)
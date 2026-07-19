from app.tools.project_scanner import ProjectScanner

scanner = ProjectScanner()

print("Python Files:")

for file in scanner.scan_python_files():

    print(file)

print("----------------")

print(

    "Total:",

    scanner.count_python_files()

)
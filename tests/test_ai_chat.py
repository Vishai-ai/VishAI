from app.ai.ai_manager import AIManager

ai = AIManager()

print("Current Provider:", ai.current_provider())

while True:

    prompt = input("\nYou : ")

    if prompt.lower() == "exit":
        break

    response = ai.generate(prompt)

    print("\nVishAI :", response)
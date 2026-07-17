from app.ai.providers.ollama_provider import OllamaProvider

ai = OllamaProvider()

while True:
    prompt = input("You : ")

    if prompt.lower() == "exit":
        break

    response = ai.generate(prompt)

    print("VishAI :", response)
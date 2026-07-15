from app.core.container import AppContainer


def main():

    container = AppContainer()

    brain = container.brain

    print("=" * 50)
    print("        Welcome to VishAI OS")
    print("=" * 50)

    while True:

        user = input("\nYou : ")

        if user.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        response = brain.think(user)

        print("VishAI :", response)


if __name__ == "__main__":
    main()
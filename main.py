from app.kernel.launcher import Launcher


def main():

    launcher = Launcher()

    launcher.initialize()

    launcher.run()

    launcher.shutdown()


if __name__ == "__main__":

    main()
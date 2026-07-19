from app.core.bootstrap import Bootstrap
from app.brain.brain_engine import BrainEngine




class Launcher:

    def __init__(self):

        self.running = False

        self.bootstrap = Bootstrap()

        self.registry = None

        self.brain = None

    def initialize(self):

        print("=" * 45)
        print("          VishAI v0.3")
        print("=" * 45)

        self.registry = self.bootstrap.initialize()

        self.brain = BrainEngine()

        self.brain.initialize()

        self.running = True
    
    
    def run(self):

        while self.running:

            command = input("\nYou > ")

            if command.lower() in ["exit", "quit"]:

                break

            try:

                response = self.brain.process(command)

                print("\n[VishAI]")

                print(response.message)
            except Exception as e:

                print("\n[ERROR]")

                print(e)


    def shutdown(self):

        if self.brain:

            self.brain.shutdown()

        print("\nShutting down VishAI...")

        self.running = False
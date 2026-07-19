from app.pipeline.response import Response


class MemoryIntent:

    def __init__(self, memory):

        self.memory = memory

    def handle(self, request):

        text = request.text.lower().strip()

        # -------------------------
        # Remember Name
        # -------------------------

        if text.startswith("my name is"):

            name = request.text[10:].strip()

            self.memory.set_fact(
                "name",
                name
            )

            return Response(
                success=True,
                message=f"Okay, I will remember your name is {name}."
            )

        # -------------------------
        # Recall Name
        # -------------------------

        if text == "what is my name" or text == "what is my name?":

            name = self.memory.get_fact("name")

            if name:

                return Response(
                    success=True,
                    message=f"Your name is {name}."
                )

            return Response(
                success=True,
                message="I don't know your name yet."
            )

        # -------------------------
        # Remember Facts
        # -------------------------

        if text.startswith("remember "):

            data = request.text[9:].strip()

            if "=" in data:

                key, value = data.split("=", 1)

                key = key.strip().lower()

                value = value.strip()

                self.memory.set_fact(
                    key,
                    value
                )

                return Response(
                    success=True,
                    message=f"I will remember that {key} is {value}."
                )

        # -------------------------
        # Recall Facts
        # -------------------------

        if text.startswith("what is "):

            key = request.text[8:].strip().lower()

            value = self.memory.get_fact(key)

            if value:

                return Response(
                    success=True,
                    message=f"{key} is {value}."
                )

        return None
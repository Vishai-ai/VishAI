from app.pipeline.response import Response


class AIIntent:

    def __init__(self, ai, knowledge):

        self.ai = ai
        self.knowledge = knowledge

    def handle(self, request):

        # Search local knowledge first

        knowledge = self.knowledge.search(
            request.text
        )

        if knowledge is not None:

            return Response(

                success=True,

                message=knowledge

            )

        # AI Fallback

        response = self.ai.generate(
            request.text
        )

        return Response(

            success=True,

            message=response

        )
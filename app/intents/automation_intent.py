from app.pipeline.response import Response


class AutomationIntent:

    def __init__(self, planner, executor):

        self.planner = planner
        self.executor = executor

    def handle(self, request):

        plan = self.planner.create_plan(
            request.text
        )

        results = self.executor.execute(
            plan
        )

        if isinstance(results, list):

            message = "\n".join(results)

        else:

            message = str(results)

        return Response(

            success=True,

            message=message

        )
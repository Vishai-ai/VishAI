from app.pipeline.response import Response


class AutomationIntent:
    """
    Handles automation requests.
    """

    def __init__(self, planner, executor):

        self.planner = planner
        self.executor = executor

    def handle(self, request):

        # Use parsed command from BrainEngine
        parsed = request.parsed_command

        plan = self.planner.create_plan(parsed)

        results = self.executor.execute(plan)

        if isinstance(results, list):
            message = "\n".join(str(r) for r in results)
        else:
            message = str(results)

        return Response(
            success=True,
            message=message
        )
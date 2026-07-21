from app.pipeline.response import Response
from app.brain.command_parser import CommandParser


class AutomationIntent:
    """
    Handles automation requests.
    """

    def __init__(self, planner, executor):

        self.parser = CommandParser()

        self.planner = planner

        self.executor = executor

    def handle(self, request):

        # Parse command
        parsed = self.parser.parse(request.text)

        # Build execution plan
        plan = self.planner.create_plan(parsed)

        # Execute
        results = self.executor.execute(plan)

        if isinstance(results, list):

            message = "\n".join(str(r) for r in results)

        else:

            message = str(results)

        return Response(

            success=True,

            message=message

        )
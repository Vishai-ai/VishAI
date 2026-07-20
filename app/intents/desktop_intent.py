from app.desktop.desktop_service import DesktopService
from app.pipeline.response import Response


class DesktopIntent:

    def __init__(self):

        self.desktop = DesktopService()

    def handle(self, request):

        success, message = self.desktop.execute(
            request.text
        )

        return Response(

            success=success,

            message=message

        )
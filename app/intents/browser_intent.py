from app.pipeline.response import Response
from app.browser.browser_manager import BrowserManager


class BrowserIntent:

    def __init__(self):

        self.browser = BrowserManager()

    def handle(self, request):

        text = request.text.lower().strip()

        # ---------------- Open Websites ----------------

        if "youtube" in text:

            return Response(
                success=True,
                message=self.browser.open_youtube()
            )

        if "google" in text:

            return Response(
                success=True,
                message=self.browser.open_google()
            )

        if "github" in text:

            return Response(
                success=True,
                message=self.browser.open_github()
            )

        if "gmail" in text:

            return Response(
                success=True,
                message=self.browser.open_gmail()
            )

        # ---------------- Google Search ----------------

        if text.startswith("search "):

            query = request.text[7:].strip()

            return Response(
                success=True,
                message=self.browser.google_search(query)
            )

        return None
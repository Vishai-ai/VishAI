import webbrowser

from app.core.logger import logger


class BrowserAutomation:
    """Handles browser automation."""

    def open_website(self, url: str):
        try:
            if not url.startswith("http"):
                url = "https://" + url

            webbrowser.open(url)

            logger.info(f"Opened website: {url}")

            return f"Opening {url}"

        except Exception as e:
            logger.error(e)
            return "Failed to open website."
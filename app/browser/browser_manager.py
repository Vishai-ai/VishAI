import webbrowser
import urllib.parse


class BrowserManager:
    """
    Browser Automation Manager
    """

    def open_url(self, url: str):

        webbrowser.open(url)

        return f"Opened {url}"

    def open_google(self):

        return self.open_url(
            "https://www.google.com"
        )

    def open_youtube(self):

        return self.open_url(
            "https://www.youtube.com"
        )

    def open_github(self):

        return self.open_url(
            "https://github.com"
        )

    def open_gmail(self):

        return self.open_url(
            "https://mail.google.com"
        )

    def search_google(self, query: str):

        url = (
            "https://www.google.com/search?q="
            + urllib.parse.quote(query)
        )

        return self.open_url(url)

    def search_youtube(self, query: str):

        url = (
            "https://www.youtube.com/results?search_query="
            + urllib.parse.quote(query)
        )

        return self.open_url(url)
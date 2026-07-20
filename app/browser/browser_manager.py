import webbrowser
from urllib.parse import quote_plus


class BrowserManager:
    """
    Handles browser automation.
    """

    def open_url(self, url: str):

        webbrowser.open(url)

        return f"Opening {url}"

    def google_search(self, query: str):

        url = f"https://www.google.com/search?q={quote_plus(query)}"

        webbrowser.open(url)

        return f"Searching Google for '{query}'"

    def youtube_search(self, query: str):

        url = f"https://www.youtube.com/results?search_query={quote_plus(query)}"

        webbrowser.open(url)

        return f"Searching YouTube for '{query}'"

    def open_youtube(self):

        return self.open_url("https://www.youtube.com")

    def open_google(self):

        return self.open_url("https://www.google.com")

    def open_github(self):

        return self.open_url("https://github.com")

    def open_gmail(self):

        return self.open_url("https://mail.google.com")
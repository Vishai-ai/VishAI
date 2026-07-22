import webbrowser

from urllib.parse import quote_plus

from app.browser.website_registry import WebsiteRegistry


class BrowserManager:

    def __init__(self):

        self.registry = WebsiteRegistry()

    # --------------------------
    # Open Website
    # --------------------------

    def open_site(self, site):

        site = site.lower().strip()

        url = self.registry.get(site)

        if url:

            webbrowser.open(url)

            return f"Opened {site}."

        # Domain name already

        if "." in site:

            webbrowser.open(

                "https://" + site

            )

            return f"Opened {site}."

        # Google Search fallback

        webbrowser.open(

            "https://www.google.com/search?q="

            + quote_plus(site)

        )

        return f"Searching Google for '{site}'."

    # --------------------------
    # Google Search
    # --------------------------

    def search_google(self, query):

        url = (

            "https://www.google.com/search?q="

            + quote_plus(query)

        )

        webbrowser.open(url)

        return f"Searching Google for '{query}'."

    # --------------------------
    # YouTube Search
    # --------------------------

    def search_youtube(self, query):

        url = (

            "https://www.youtube.com/results?search_query="

            + quote_plus(query)

        )

        webbrowser.open(url)

        return f"Searching YouTube for '{query}'."
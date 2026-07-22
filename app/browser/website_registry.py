class WebsiteRegistry:
    """
    Registry of well-known websites.
    """

    def __init__(self):

        self.websites = {

            "google": "https://www.google.com",

            "youtube": "https://www.youtube.com",

            "github": "https://github.com",

            "chatgpt": "https://chatgpt.com",

            "openai": "https://openai.com",

            "gmail": "https://mail.google.com",

            "facebook": "https://facebook.com",

            "instagram": "https://instagram.com",

            "linkedin": "https://linkedin.com",

            "reddit": "https://reddit.com",

            "amazon": "https://amazon.in",

            "flipkart": "https://flipkart.com",

            "stackoverflow": "https://stackoverflow.com",

            "x": "https://x.com",

            "twitter": "https://x.com",

            "python": "https://python.org",

            "wikipedia": "https://wikipedia.org"

        }

    def get(self, name: str):

        return self.websites.get(name.lower())

    def exists(self, name: str):

        return name.lower() in self.websites
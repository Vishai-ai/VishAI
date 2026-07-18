class KnowledgeBase:
    """
    Stores built-in knowledge that can be
    expanded later with databases, PDFs,
    web search and vector memory.
    """

    def __init__(self):

        self.data = {

            "python":
                "Python is a high-level programming language.",

            "vishai":
                "VishAI is an AI Operating System under development.",

            "ai":
                "Artificial Intelligence enables machines to learn and solve problems."

        }

    def search(self, query: str):

        query = query.lower()

        for key, value in self.data.items():

            if key in query:

                return value

        return None
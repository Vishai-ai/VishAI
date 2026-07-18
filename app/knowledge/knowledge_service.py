from app.knowledge.knowledge_base import KnowledgeBase


class KnowledgeService:
    """
    High-level interface between BrainEngine and KnowledgeBase.
    """

    def __init__(self):

        self.knowledge = KnowledgeBase()

    def search(self, query: str):

        return self.knowledge.search(query)
from app.memory.memory_manager import MemoryManager


class MemoryService:
    """
    High level interface used by BrainEngine.
    """

    def __init__(self):

        self.manager = MemoryManager()

    # ===================================================
    # Notes
    # ===================================================

    def remember(self, note: str):

        self.manager.add_note(note)

    def get_notes(self):

        return self.manager.get_notes()

    # ===================================================
    # Facts
    # ===================================================

    def remember_fact(self, key: str, value: str):

        self.manager.set_fact(key, value)

    def recall_fact(self, key: str):

        return self.manager.get_fact(key)

    # ---------------------------------------------------
    # Aliases (For BrainEngine)
    # ---------------------------------------------------

    def set_fact(self, key: str, value: str):

        self.manager.set_fact(key, value)

    def get_fact(self, key: str):

        return self.manager.get_fact(key)

    # ===================================================
    # User
    # ===================================================

    def get_user_name(self):

        return self.manager.get_user_name()

    def set_user_name(self, name: str):

        self.manager.set_user_name(name)
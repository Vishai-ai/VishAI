from enum import Enum


class Intent(Enum):
    AI_CHAT = "ai_chat"

    AUTOMATION = "automation"

    MEMORY = "memory"

    KNOWLEDGE = "knowledge"

    CODING = "coding"

    SEARCH = "search"

    FILE = "file"

    VISION = "vision"

    VOICE = "voice"

    SETTINGS = "settings"

    UNKNOWN = "unknown"
from enum import Enum


class AIProvider(Enum):
    OLLAMA = "ollama"
    GEMINI = "gemini"
    OPENAI = "openai"
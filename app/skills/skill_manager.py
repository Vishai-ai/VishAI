from app.skills.calculator_skill import CalculatorSkill
from app.skills.browser_skill import BrowserSkill


class SkillManager:
    """Manages all VishAI skills."""

    def __init__(self):
        self.skills = {
            "calculator": CalculatorSkill(),
            "browser": BrowserSkill(),
        }

    def get_skill(self, name: str):
        return self.skills.get(name)
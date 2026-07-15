from app.skills.base_skill import BaseSkill


class CalculatorSkill(BaseSkill):

    def execute(self, command: str):
        return "Calculator Skill"
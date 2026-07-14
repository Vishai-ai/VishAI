from app.skills.base_skill import BaseSkill


class AutomationSkill(BaseSkill):

    def execute(self, command: str):
        return "Automation Skill"
from app.skills.base_skill import BaseSkill


class BrowserSkill(BaseSkill):

    def execute(self, command: str):
        return "Browser Skill"
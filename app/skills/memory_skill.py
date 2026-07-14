from app.skills.base_skill import BaseSkill


class MemorySkill(BaseSkill):

    def execute(self, command: str):
        return "Memory Skill"
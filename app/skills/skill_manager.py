class SkillManager:

    def __init__(self):

        self.skills = []

    def register(self, skill):

        self.skills.append(skill)

    def execute(self, text):

        for skill in self.skills:

            if skill.can_handle(text):

                return skill.execute(text)

        return None
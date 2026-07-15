from app.skills.skill_manager import SkillManager

manager = SkillManager()

print(manager.get_skill("calculator").execute(""))
print(manager.get_skill("browser").execute(""))
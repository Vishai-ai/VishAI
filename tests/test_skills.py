from app.skills.memory_skill import MemorySkill
from app.skills.automation_skill import AutomationSkill

memory = MemorySkill()
automation = AutomationSkill()

print(memory.execute("remember"))
print(automation.execute("open calculator"))

#An interface for each unit that is placed within the game
#Written by Greg Suner
class Unit

	
	#__init__ unit properties
	def __init__(self,personal,job,tempStats,inventory,currentHp,skills):
		self.personal = personal
		self.job = job
		self.tempStats = tempStats
		self.inventory = inventory
		self.currentHp = currentHp
		self.skills = skills
		
	
	#Returns units statlist
	def ask_stats(self):
		pass
	
	#Takes int to select which specific stat to return
	#Returns specified stat
	def ask_stat?(self, statId):
		pass
	
	#Takes a weapon as a parameter to check if this unit can equip it
	#Returns a boolean
	def ask_equippible(self, weapon):
		pass
	
	#Sets weapon to indicated slotNum within unit inventory
	def equip(self, item, slotNum):
		pass
	
	#Asks if a unit can have a certain skill
	def ask_equip_skills(self):
		pass
	
	

	
	
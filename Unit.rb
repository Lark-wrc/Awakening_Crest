#An interface for each unit that is placed within the game
class Unit

	attr_accessor :personal,:job,:tempStats,:inventory,:currentHp,:activeSkills
	
	#__init__ unit properties
	def __init__(self,personal,job,tempStats,inventory,currentHp,skills)
		self.personal = personal
		self.job = job
		self.tempStats = tempStats
		self.inventory = inventory
		self.currentHp = currentHp
		self.skills = skills
		
	
	#Returns units statlist
	def ask_stats()
	
	
	#Takes int to select which specific stat to return
	#Returns specified stat
	def ask_stat?(statId)
	
	
	#Takes a weapon as a parameter to check if this unit can equip it
	#Returns a boolean
	def ask_equippible(self, weapon)
	
	
	#Sets weapon to indicated slotNum within unit inventory
	def equip(item, slotNum)
	
	
	#Asks if a unit can have a certain skill
	def ask_equip_skills
	
	
	

	
	
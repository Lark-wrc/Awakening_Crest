#An interface for each unit that is placed within the game
#Written by Greg Suner
class Unit

<<<<<<< HEAD:Unit.rb
	attr_accessor ):personal,):job,):tempStats,):inventory,):currentHp,):activeSkills
=======
>>>>>>> origin/master:Unit.py
	
	#__init__ unit properties
	def __init__(self,personal,job,tempStats,inventory,currentHp,skills):
		self.personal = personal
		self.job = job
		self.tempStats = tempStats
		self.inventory = inventory
		self.currentHp = currentHp
		self.skills = skills
		
	
	#Returns units statlist
<<<<<<< HEAD:Unit.rb
	def ask_stats():
	
	
	#Takes int to select which specific stat to return
	#Returns specified stat
	def ask_stat?(statId):
	
=======
	def ask_stats(self):
		pass
	
	#Takes int to select which specific stat to return
	#Returns specified stat
	def ask_stat?(self, statId):
		pass
>>>>>>> origin/master:Unit.py
	
	#Takes a weapon as a parameter to check if this unit can equip it
	#Returns a boolean
	def ask_equippible(self, weapon):
<<<<<<< HEAD:Unit.rb
	
	
	#Sets weapon to indicated slotNum within unit inventory
	def equip(item, slotNum):
	
=======
		pass
	
	#Sets weapon to indicated slotNum within unit inventory
	def equip(self, item, slotNum):
		pass
>>>>>>> origin/master:Unit.py
	
	#Asks if a unit can have a certain skill
	def ask_equip_skills(self):
		pass
	
	

	
	
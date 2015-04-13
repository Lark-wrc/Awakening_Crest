from Statlist import Statlist
from pprint import pprint
#An interface for each unit that is placed within the game
#Written by Greg Suner
class Unit(object):
	#__init__ unit properties
	def __init__(self,personal,job,tempStats,inventory,currentHp,skills):
		self.personal = personal
		self.job = job
		self.tempStats = Statlist(*tempStats)
		self.inventory = inventory
		self.currentHp = currentHp
		self.skills = skills
		self.grey = False
		self.currRange = 0
		self.equipped = None
	
	#Returns units statlist
	def ask_stats(self):
		pass
	
	#Takes int to select which specific stat to return
	#Returns specified stat
	def ask_stat(self, statId):
		if statId == 'def':
			if self.personal.gains.defense > self.job.maxClassStat.defense+self.personal.maxStats.defense:
				defense = self.job.maxClassStat.defense+self.personal.maxStats.defense
			else: 
				defense = self.personal.gains.defense 
			return defense
		elif statId == 'luck':
			if self.personal.gains.luck > self.job.maxClassStat.luck+self.personal.maxStats.luck:
				luck = self.job.maxClassStat.luck+self.personal.maxStats.luck
			else: 
				luck = self.personal.gains.luck
			return luck
		elif statId == 'spd':
			if self.personal.gains.speed > self.job.maxClassStat.speed+self.personal.maxStats.speed:
				speed = self.job.maxClassStat.speed+self.personal.maxStats.speed
			else: 
				speed = self.personal.gains.speed
			return speed
		elif statId == 'mov':
			return self.personal.movement
		else:
			return None

	
	#Takes a weapon as a parameter to check if this unit can equip it
	#Returns a boolean
	def ask_equippible(self, weapon):
		if weapon.equippible() in self.job.profics:
			return 1
		else:
			return 0
	
	#Sets weapon to indicated slotNum within unit inventory
	def equip(self, slot):
		if self.ask_equippible(self.inventory.container[slot]):
			self.equipped = self.inventory.container[slot]
			self.equipped.on_equip(self)
			
	
	#Asks if a unit can have a certain skill
	def ask_equip_skills(self):
		pass
		
	def resetTemps(self):
		self.tempStats =  Statlist(*[0,0,0,0,0,0,0,0])
	
	def printout(self):
		pprint (vars(self))
		pprint (vars(self.personal))
		pprint (vars(self.job))

	def properties(self):
		#attack
		ret = []
		ret.append(0)
		if self.personal.gains.str > self.job.maxClassStat.str+self.personal.maxStats.str:
			ret[0] = self.job.maxClassStat.str+self.personal.maxStats.str
		else: 
			ret[0] = self.personal.gains.str
		ret[0] += self.equipped.mt#+rank bonus
		
		ret.append(0)
		if self.personal.gains.skill > self.job.maxClassStat.skill+self.personal.maxStats.skill:
			skill = self.job.maxClassStat.skill+self.personal.maxStats.skill
		else: 
			skill = self.personal.gains.skill
		if self.personal.gains.luck > self.job.maxClassStat.luck+self.personal.maxStats.luck:
			luck = self.job.maxClassStat.luck+self.personal.maxStats.luck
		else: 
			luck = self.personal.gains.luck
		ret[1] = self.equipped.hit + (skill*3+luck)/2#+rank bonus
		
		ret.append(0)
		ret[2] = self.equipped.crit + skill/2
		
		ret.append(0)
		if self.personal.gains.speed > self.job.maxClassStat.speed+self.personal.maxStats.speed:
			speed = self.job.maxClassStat.speed+self.personal.maxStats.speed
		else: 
			speed = self.personal.gains.speed
		ret[3] = (speed*3+luck)/2
		
		return ret
			
	
	
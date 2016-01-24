from Statlist import Statlist
from pprint import pprint

class Unit(object):
	"""Author: Greg Suner and Bill Clark, Authors as noted.
		Purpose:The top level container for a game unit. Units are made of a personnel file, with a character's
		values, and the class information, titled as job in the writing. Unit's methods are used to manage the
		stats from both of these sets and return their totals or modifications. An interface in the literal sense,
		not the CS sense.
	"""
	def __init__(self,personal,job,tempStats,inventory,currentHp,skills, position):
		"""Author: Greg Suner
		Purpose:Constructor.
		"""
		self.personal = personal
		self.job = job
		self.tempStats = Statlist(*tempStats)
		self.inventory = inventory
		self.currentHp = currentHp
		self.skills = skills
		self.grey = False
		self.currRange = 0
		self.equipped = None
		self.position = position

	#Takes int to select which specific stat to return
	#Returns specified stat
	def ask_stat(self, statId):
		"""Author: Bill Clark
		Purpose: Gives the calculated stats for a given stat based off the personal and job files for the unit.
				Stats cap at a number specified in personal, so this makes sure the stat is legal.
		Return: the stat asked for.
		"""
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
	def canEquip(self, weapon):
		"""Author: Bill Clark
		Purpose: Check if this unit may equip a weapon type.
		Return: Bool
		"""
		if (weapon.type in self.job.profics) and :
			return 1
		else:
			return 0
	
	#Sets weapon to indicated slotNum within unit inventory
	def equip(self, slot):
		"""Author: Bill Clark
		Purpose:Equips an item to this unit, if it is able to. Applies all changes to the unit's values.
		"""

		if self.ask_equippible(self.inventory.container[slot]):
			self.equipped = self.inventory.container[slot]
			self.equipped.on_equip(self)
			self.currRange = self.equipped.range
			
	
	#Asks if a unit can have a certain skill
	def ask_equip_skills(self):
		"""Unused with current feature set."""
		pass
		
	def resetTemps(self):
		"""Author: Bill Clark
		Purpose:If an effect gives a temporary effect to a unit, it's stored in the tempstats list. This method
				resets them, as they only last until next turn. Technically unnecessary.
		Return: A forecast.
		"""
		self.tempStats =  Statlist(*[0,0,0,0,0,0,0,0])
	
	def printout(self):
		"""Author: Bill Clark
		Purpose: To string, basically. Choppy, mainly for testing.
		Return:
		"""
		pprint (vars(self))
		pprint (vars(self.personal))
		pprint (vars(self.job))

	def properties(self):
		"""Author: Bill Clark
		Purpose: Returns the combat stats of a unit. These are calculated based off the units stats, equipment stats,
				and etc. They are attack, hit rate, avoid, and critical chance.
		"""
		ret = []
		ret.append(0)
		if self.personal.gains.str > self.job.maxClassStat.str+self.personal.maxStats.str:
			ret[0] = self.job.maxClassStat.str+self.personal.maxStats.str
		else: 
			ret[0] = self.personal.gains.str
		ret[0] += self.equipped.mt #+rank bonus
		
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
			
	
	
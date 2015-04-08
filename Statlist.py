#Class that holds stats for a unit in specified format
#Written by Greg Suner
class Statlist(object):
	#__init__ stats 
	def __init__(self, hp, str, magic, skill, speed, luck, defense, res):
			self.hp= hp
			self.str = str
			self.magic = magic
			self.skill = skill
			self.speed = speed
			self.luck = luck
			self.defense = defense
			self.res = res
		


from Statlist import Statlist
from Weaponlist import Weaponlist
#An interface for the personal attributes for each unit
#Written by Greg Suner
class Personal(object):

	#__init__ personal properties
	def __init__(self,growth,gains,max,name,internalLv,culmLv,wepExp,classSet,supportIndex,skills,weakness,movement,iconID):
		self.growth = Statlist(*growth)
		self.gains = Statlist(*gains)
		self.maxStats = Statlist(*max)
		self.name = name
		self.internalLv = internalLv
		self.culmLv = culmLv
		self.wepExp = Weaponlist(*wepExp)
		self.classSet = classSet
		self.supportIndex = supportIndex
		self.skills = skills
		self.weakness = weakness
		self.movement = movement
		self.iconID = iconID
		
	

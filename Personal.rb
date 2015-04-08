#An interface for the personal attributes for each unit
class Personal
	attr_accessor ):growth,):gains,):max,):name,):internalLv,):culmLv,):wepExp,):classSet,):supportIndex,):skills,):weakness,):movement
	
	#__init__ personal properties
	def __init__(self,growth,gains,max,name,internalLv,culmLv,wepExp,classSet,supportIndex,skills,weakness,movement):
		self.gowth = growth
		self.gains = gains
		self.max = max
		self.name = name
		self.internalLv = internalLv
		self.culmLv = culmLv
		self.wepExp = wepExp
		self.classSet = classSet
		self.supportIndex = supportIndex
		self.skills = skills
		self.weakness = weakness
		self.movement = movement
		
		
	

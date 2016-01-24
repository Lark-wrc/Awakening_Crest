from Statlist import Statlist
class Fe_Class:
	"""Author: Greg Suner
	Purpose: Stores information about a class that unit may be a member of.
	"""
	def __init__(self,maxClassStat,currentLv,exp,promote,lvCap,promoteLv, promotions, name, profics):
		self.maxClassStat = Statlist(*maxClassStat)
		self.currentLv = currentLv
		self.exp = exp
		self.promote = promote
		self.lvCap = lvCap
		self.promoteLv = promoteLv
		self.promotions = promotions
		self.name = name
		self.profics = profics
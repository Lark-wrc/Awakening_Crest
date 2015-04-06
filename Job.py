#An interface for all job types that a unit can have
#Written by Greg Suner
class Job
	
	#__init__ class properties
	def __init__(self,maxClassStat,currentLv,exp,promote,lvCap,promoteLv, promotions, name, profics)
		self.maxClassStat = maxClassStat
		self.currentLv = currentLv
		self.exp = exp
		self.promote = promote
		self.lvCap = lvCap
		self.promoteLv = promoteLv
		self.promotions = promotions
		self.name = name
		self.profics = profics
	

#An interface for all class(job) types that a unit can have
class Class
	attr_accessor :maxClassStat,:currentLv,:exp,:promote,:lvCap,:promoteLv,:promotions,:name,:profics
	
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
	

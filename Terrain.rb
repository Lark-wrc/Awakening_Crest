class Terrain
	attr_accessor :defen,:hit,:cost,:heal,:iconID
	
	def __init__(self,defen, hit, cost, heal, iconID)
		self.defen = defen
		self.hit = hit
		self.cost = cost
		self.heal = heal
		self.iconID = iconID
		
	
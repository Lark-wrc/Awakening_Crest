
class Terrain(object):
	"""Author: Bill Clark
		Purpose: Holds all values associated with a single square of terrain.
	"""
	def __init__(self, defen, hit, heal, cost, name, iconID):
		self.defen = defen
		self.hit = hit
		self.cost = cost
		self.heal = heal
		self.name = name
		self.iconID = iconID
		
	
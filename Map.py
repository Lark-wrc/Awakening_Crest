import json
import pickle
from Terrain import Terrain
class Map(Object):
	def __init__(self, file_map, file_data, file_terrain, file_player):
		jsonObj = json.load(open(file_map,'r'))
		self.player_file = json.load(open(player,'r'))
		self.xDim = jsonObj['X_Dim']
		self.yDim = jsonObj['Y_Dim']
		self.armyCounts = jsonObj['Unit_Counts']
		
		self.grid = parse(jsonObj['Legend'], jsonObj['Map'], file_terrain)
		assert(None not in grid)
		self.units = [[None for i in range(0,self.xDim)] for i in range(0,self.yDim)]
		
		self.playerArmy	= None
		self.otherArmies = []
		army_setup(file_player, file_data)
		
		self.events = resolveEvents(file_data)
		
	#possibly via A*
	#calculated the cost of travelling from the ordered pair to start to the same end. 
	#This takes into account the cost of each square in the grid. The cost might be stored differently,
	#so don't start quite yet. 
	def distance(self, start, end):
		pass
	
	#Find out if something (type) is accessible from where it is. This includes range, so it's always
	#one larger than reachable. possible refactoring to show that. Basically, this is for is X in my attack
	#range?
	def in_prox(self, source, type, range):
		pass
	#returns something related to things that this unit is in proximity too. Remember, proximity doesn't mean
	#you can reach that square, it means that you can get within range of it, with specified range.
	def proximity(self, source, type, range):
		pass
	#returns something. Probably a list of all squares a source can reach. maybe.
	def reachable(self, source, end):
		pass
	#can thing in source move to ordered pair end in one move?
	def is_reachable(self, start, end):
		pass
	
	def parse(self, legend, map, file):
		grid = [[None for i in range(0,self.xDim)] for i in range(0,self.yDim)]
		terrains = json.load(open(file,'r'))
		for x in range(0, self.xDim):
			for y in range(0, self.yDim):
				terra = legend[ map[x][y] ]
				grid[x][y] = Terrain(*terrains[terra])
		
		return grid
	def army_setup(self, player, data):
		data_file = json.load(open(data,'r'))
		self.playerArmy = pickle.load(player_file['army'])
		for x in data_file['army']:
			self.otherArmies.append(pickle.load(data_file['Armies']))
		
		for x in data_file['Starting_Pos'][0]:
			units[x[0]][x[1]] = self.playerArmy.army.pop()
		for x in range(1,len(data_file['Starting_Pos']):
			for y in data_file['Starting_Pos'][x]:
				units[y[0],y[1]] = otherArmies[x-1].army.pop()
	def resolveEvents(self, file):
		pass
	
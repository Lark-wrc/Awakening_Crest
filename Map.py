import json
import pickle
from Terrain import Terrain
class Map(object):
	def __init__(self, file_map, file_data, file_player):
		jsonObj = json.load(open(file_map,'r'))
		#self.player_file = pickle.load(open(file_player,'r'))
		self.xDim = jsonObj['X_Dim']
		self.yDim = jsonObj['Y_Dim']
		
		
		self.grid = self.parse(jsonObj['Legend'], jsonObj['Map'])
		assert(None not in self.grid)
		self.units = [[None for i in range(0,self.xDim)] for i in range(0,self.yDim)]
		
		self.playerArmy	= None
		self.otherArmies = []
		self.army_setup(file_player, file_data)
		
		
		self.events = self.resolveEvents(file_data)
		
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
	
	#Parses the grid. Using the legend provided, it checks the map symbols against the terrain type
	#file. it place the correct type of terrain in that square, and moves on.
	def parse(self, legend, map):
		grid = [[None for i in range(0,self.xDim)] for i in range(0,self.yDim)]
		terrains = json.load(open('Terrain_Types.json','r'))
		for x in range(0, self.xDim):
			for y in range(0, self.yDim):
				terra = legend[ map[x][y] ]
				grid[x][y] = Terrain(*terrains[terra])
		
		return grid
		
	#Loads all information based on the map data file, all armies, and deploys inital units.
	def army_setup(self, player, data):
		#declarations from the map's associated data file.
		data_file = json.load(open(data, 'r'))
		self.playerArmy = pickle.load(open(player))
		self.armyCounts = data_file['Unit_Counts']
		self.preBattle = data_file['Pre_Battle']
		
		#loads all the other armies, incase of more than 2.
		for x in data_file['Armies']:
			self.otherArmies.append(pickle.load(open(x)))
		
		#for each starting pos x, place the next unit in the army there. IE, deploy the top
		#armyCount.
		for x in data_file['Starting_Pos'][0]:
			for y in range(0,self.armyCounts[0]):
				self.units[x[0]-1][x[1]-1] = self.playerArmy.units[y]
		#Same as above, extra loop for each of the non player armies.
		for x in range(1,len(data_file['Starting_Pos'])):
			for y in data_file['Starting_Pos'][x]:
				for z in range(0,self.armyCounts[x-1]):
					self.units[y[0]-1][y[1]-1] = self.otherArmies[x-1].units[z]
		
	def resolveEvents(self, file):
		return []
	
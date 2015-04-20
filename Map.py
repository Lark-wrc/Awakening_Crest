import json
import pickle
from Unit import Unit
from Terrain import Terrain
test = False


class Map(object):
	"""Author: Greg Suner and Bill Clark, method authors noted.
		Purpose: Holds most of the information for a game level. The map, AI information, armies... and so on.
	"""

	def __init__(self, file_map, file_data, file_player):
		"""Author: Bill Clark
		Purpose: Constructor. Uses three json files to upload information. Doles out some information loading
				to the map parse and army setup methods.
		"""
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

	def in_prox(self, source, type, range):
		"""Author: Bill Clark, Greg Suner's reachable as a base.
		Purpose: This method checks if a particular type of thing is within range of a unit. This includes
				if the target is within range beyond movement area. It returns true at the first instance of
				something in range.
		"""
		unitRange = range
		xDim = source[0]
		yDim = source[1]
		squares = self.squares(xDim,yDim,unitRange+source.equipped.range)
		for target in squares:
			if type == 'unit' and isinstance(self.units[target[0]][target[1]], Unit) and tuple(source) != target:
				return True
			elif type == 'players' and isinstance(self.units[target[0]][target[1]], Unit) and tuple(source) != target \
				and self.units[target[0]][target[1]] in self.playerArmy.units:
				return True

	def proximity(self, source, type, range):
		"""Author: Bill Clark, Greg Suner's reachable as base.
		Purpose: Functions much like in_prox, this method returns the coordinates of the targets found.
		"""
		unitRange = range
		xDim = source[0]
		yDim = source[1]
		squares = self.squares(xDim,yDim,unitRange)
		inRange = []
		for target in squares:
			if type == 'unit' and isinstance(self.units[target[0]][target[1]], Unit) and tuple(source) != target:
				inRange.append(target)
			elif type == 'players' and isinstance(self.units[target[0]][target[1]], Unit) and tuple(source) != target \
				and self.units[target[0]][target[1]] in self.playerArmy.units:
				inRange.append(target)
		if test: print inRange
		return inRange

	def squares(self, currX, currY, mov):
		"""Author: Bill Clark
		Purpose: This method generates a list of all the coordinates, in a perfect world, a unit can range with it's
				movement speed. It returns them in a list. Does not return values outside the grid.
		"""
		ret = []
		up = True
		ys = -1 #y adjustment from the baseline x row.
		for col in range(-mov,mov+1): #added one to include center space
			if ys < mov and up:
				ys+=1
			elif ys == mov:
				ys-=1
				up = False
			elif ys > 0 and not up:
				ys-=1
			elif ys <= 0:
				ys+=1
				up = True
			else:
				print 'derp'
			#print ys, "ys"
			for row in range(1,ys+1): #eliminates zeros
				if currX+col >= 0 and currX+col < self.xDim and row+currY < self.yDim and row+currY >= 0:
					ret.append((currX+col, row+currY))
				if currX+col >= 0 and currX+col < self.xDim and -row+currY < self.yDim and -row+currY >= 0:
					ret.append((currX+col, -row+currY))
			if currX+col >= 0 and currX+col < self.xDim and currY < self.yDim and currY >= 0:
				ret.append((currX+col, currY))
		if test: print ret
		return ret

	def reachable(self, source,location, end):
		"""Author: Greg Suner
		Purpose: Returns a list of all locations a unit can move to.
		"""
		unitRange = source.ask_stat('mov')
		xDim = location[0]
		yDim = location[1]
		squares = self.squares(xDim,yDim,unitRange)
		inRange = []
		#use A* to check with movement costs of terrain
		for target in squares:
			path, cost = self.get_best_path(source, location, target)
			if cost<=unitRange and self.units[target[0]][target[1]] == None or self.units[target[0]][target[1]] == source:
				inRange.append(target)
		return inRange.append(tuple(location))
		

	def is_reachable(self, source, start, end):
		"""Author: Greg Suner
		Purpose: Given a target location, return if the specified unit can reach it from it's starting point.
		"""
		path, range = self.get_best_path(source, start, end)
		if end[0] == start[0] and end[1] == start[1]:
			return 1
		elif range[end] <= source.ask_stat('mov') and self.units[end[0]][end[1]] == None:
			return 1
		else:
			return 0
			
	
#example from online
	
	def get_best_path(self, source, current, goal):
		"""Author: Modifications of example for our situation, Greg Suner., Data Structure redesign for our needs, Bill Clark.
		Purpose: The A* heuristic. Returns the path it took and the cost to there.
		"""
		frontier = {}
		frontier[current] = 0
		came_from = {}
		cost_so_far = {}
		came_from[current] = None
		cost_so_far[current] = 0

		while len(frontier) > 0:
			res = sorted(frontier, key=frontier.get)
			current = res[0]
			del frontier[current]
			if current == goal:
				#return the path
				break
		   
			for next in self.squares(current[0],current[1],1):
				new_cost = cost_so_far[current] + self.grid[next[0]][next[1]].cost
				if next not in cost_so_far or new_cost < cost_so_far[next]:
					cost_so_far[next] = new_cost
					priority = new_cost + self.heuristic(goal, next)
					frontier[next] = priority
					came_from[next] = current
		return came_from, cost_so_far

	def heuristic(self, goal, current):
		"""Author: Greg Suner
		Purpose: Manhattan heuristic.
		"""
		x = abs(goal[0]-current[0])
		y = abs(goal[1]-current[1])
		return x+y

	def cost(self, next):
		"""Author: Bill Clark
		Purpose: Returns the cost of a given location.
		"""
		x = next[0]
		y = next[1]
		return self.grid[x][y].cost

	
	#Parses the grid. Using the legend provided, it checks the map symbols against the terrain type
	#file. it place the correct type of terrain in that square, and moves on.
	def parse(self, legend, map):
		"""Author: Bill Clark
		Purpose: Using the legend from the map file, as well as the map array, create a double array of
				terrain pieces, otherwise, the game map.
		"""
		grid = [[None for i in range(0,self.xDim)] for i in range(0,self.yDim)]
		terrains = json.load(open('Terrain_Types.json','r'))
		for x in range(0, self.xDim):
			for y in range(0, self.yDim):
				terra = legend[ map[x][y] ]
				grid[x][y] = Terrain(*terrains[terra])
		
		return grid
		
	#Loads all information based on the map data file, all armies, and deploys inital units.
	def army_setup(self, player, data):
		"""Author: Bill Clark
		Purpose: Loads the armies in the data file and places them in the starting positions.
				Also loads the other data file information for the whole map.
		"""
		#declarations from the map's associated data file.
		data_file = json.load(open(data, 'r'))
		self.playerArmy = pickle.load(open(player))
		self.armyCounts = data_file['Unit_Counts']
		self.preBattle = data_file['Pre_Battle']
		self.persona = data_file["Persona"]

		#loads all the other armies, incase of more than 2.
		for x in data_file['Armies']:
			self.otherArmies.append(pickle.load(open(x)))
		
		#for each starting pos x, place the next unit in the army there. IE, deploy the top
		#armyCount.
			for i, y in enumerate(data_file['Starting_Pos'][0]):
				self.units[y[0]-1][y[1]-1] = self.playerArmy.units[i]
		#Same as above, extra loop for each of the non player armies.
		for x in range(1,len(data_file['Starting_Pos'])):
			for i, y in enumerate(data_file['Starting_Pos'][x]):
				self.units[y[0]-1][y[1]-1] = self.otherArmies[x-1].units[i]
		
	def resolveEvents(self, file):
		"""Author: Bill Clark
		Purpose: Unused.
		"""
		return []

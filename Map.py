import json
import pickle
from Unit import Unit
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
	
	#Find out if something (type) is accessible from where it is. This includes range, so it's always
	#one larger than reachable. possible refactoring to show that. Basically, this is for is X in my attack
	#range?
	def in_prox(self, source, type, range):
		unitRange = range
		xDim = source[0]
		yDim = source[1]
		squares = self.squares(xDim,yDim,unitRange)
		for target in squares:
			if type == 'unit' and isinstance(self.units[target[0]][target[1]], Unit) and tuple(source) != target:
				return True
			elif type == 'players' and isinstance(self.units[target[0]][target[1]], Unit) and tuple(source) != target \
				and self.units[target[0]][target[1]] in self.playerArmy.units:
				return True
	#Remember, proximity doesn't mean
	#you can reach that square, it means that you can get within range of it, with specified range.
	#list of things it can get in range of ie. distance + range
	def proximity(self, source, type, range):
		unitRange = range
		xDim = source[0]
		yDim = source[1]
		#print location
		squares = self.squares(xDim,yDim,unitRange)
		#print squares
		inRange = []
		#use A* to check with movement costs of terrain
		for target in squares:
			if type == 'unit' and isinstance(self.units[target[0]][target[1]], Unit) and tuple(source) != target:
				inRange.append(target)
			elif type == 'players' and isinstance(self.units[target[0]][target[1]], Unit) and tuple(source) != target \
				and self.units[target[0]][target[1]] in self.playerArmy.units:
				inRange.append(target)
		#print inRange
		return inRange

	#Bill's diamond generation method.
	def squares(self, currX, currY, mov):
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
		#print ret
		return ret

	#Returns list of squares in range of source
	def reachable(self, source,location, end):
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
		
		
	#can thing in source move to ordered pair end in one move
	def is_reachable(self, source, start, end):
		path, range = self.get_best_path(source, start, end)
		if end[0] == start[0] and end[1] == start[1]:
			return 1
		elif range[end] <= source.ask_stat('mov') and self.units[end[0]][end[1]] == None:
			return 1
		else:
			return 0
			
	
#example from online
	
	def get_best_path(self, source, current, goal):
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

	#manhattan heuristic - total of difference of x and y	
	def heuristic(self, goal, current):
		x = abs(goal[0]-current[0])
		y = abs(goal[1]-current[1])
		return x+y
		
	#pull cost from terrain	
	def cost(self, next):
		x = next[0]
		y = next[1]
		return self.grid[x][y].cost

	
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
		return []
	

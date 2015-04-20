from Map import Map
import os
import sys
import pprint
import CombatCalc

#The game map. 
gameMap = None
turnStack = []

#Prints the map. Does this in a grid shape, 3x1 characters. uses the gameMap grid and units to process.
def printMap():
	"""Author: Bill Clark
		Purpose: Pretty prints out the game map.
	"""
	for i in range(gameMap.yDim+1):
		if i == 0:
			# column for row numbers
			print("   "),
		else:
			# column headers
			print("{0:3d} ".format(i)),
	print("")
	for i, (rowg, rowu) in enumerate(zip(gameMap.grid, gameMap.units)):
		# row number
		print("{0:2d} ".format(i+1)),
		for colg, colu in zip(rowg,rowu):
			# row data
			if colu == None:
				print(" {0:2d} ".format(colg.iconID)),
			else:
				print(" {0:2d} ".format(colu.personal.iconID)),
		print("")

def shift(seq):
	"""Author: Bill Clark
		Purpose: Shifts an array around.
	"""
	return seq[1:]+seq[:1]


def resetTempStats(units):
	"""Author: Bill Clark
		Purpose: Resets the temporary stats of all units in the given list.
	"""
	for x in units:
		x.resetTemps()

#removes grey status from all units in an army. Used to start a new turn.
def deGray(units):
	"""Author: Bill Clark
		Purpose: Reactivates all units in the given list.
	"""
	for x in units:
		#print x.personal.name, x.grey
		x.grey = False


def moveAction(map):
	""" Author: Bill Clark
	Purpose: This covers the selection of a unit by a player, selecting it's target location and moving it there.
	First of all, the stupid ducking grid likes its coordinates in y,x format. in order to be human readable,
	they are swapped at the commented section from the x, y given by the player. Not salty.
	Most of the commands in this method have no alternatives. You have one thing to do, select a unit, and if
	you can't, your done. So it's mostly a bunch of while loops that make sure you actually put in a real input.
	As far as actual commands, it goes "select", "x,y", "x,y". Say you want to move, move what, to where. If at
	anytime back is typed, it moves up a level. Also to note, "end turn" is valid at the top level, to move
	the turn order.
	"""
	cursor = (-1, -1) #basically the most recent accesed location. for internal use.
	a = raw_input("Type a command, ? for help: ")

	#Top level for, you can choose to end your turn or interact with a unit.
	while a != 'end turn':
		if a == '?':
			print "select a square with an allied unit who has not acted this turn."
			print "you can type back to go back."
		elif a == 'select':
			b = raw_input("Where are you selecting?: ")
			#Second level while, gets the coordinates you want to move to.
			while b != 'back':
				b = b.split(' ')
				#switches x and y to match y x format in the code. minus one is to accommodate front end non zero indexs.
				cat = b[0]
				b[0] = int(b[1])-1
				b[1] = int(cat)-1
				#print b[0],b[1]

				#BUNCHA checkin for target validity. specifically, if it's on the map, if it's a unit, under
				#your control, and hasn't already moved.
				if b[0] < map.xDim and b[1] < map.yDim and map.units[b[0]][b[1]] is not None and \
				map.units[b[0]][b[1]] in map.playerArmy.units and not map.units[b[0]][b[1]].grey:
					cursor = (b[0],b[1])
					c = raw_input("Where should it move?: ")
					#Lowest while, gets movement target.
					while c != 'back':
						c = c.split(' ')
						#switches x and y to match y x format in the code. minus one is to accommodate front end non zero indexs.
						cat = c[0]
						c[0] = int(c[1])-1
						c[1] = int(cat)-1

						#target validity checking...
						if c[0] < map.xDim and c[1] < map.yDim \
						and map.is_reachable(map.units[b[0]][b[1]], cursor, (c[0], c[1])):
							cursor = (c[0],c[1])
							if cursor != tuple([b[0],b[1]]):
								map.units[c[0]][c[1]] = map.units[b[0]][b[1]]
								map.units[b[0]][b[1]] = None
							os.system('cls' if os.name == 'nt' else 'clear')
							printMap()

							#This returns 1 if back is sent from the action menus. Which will continue this
							#loop. If 0 is sent, it's actually reccuring up the stack with the end turn command.
							if actionAction(map,cursor, map.units[c[0]][c[1]]):
								if cursor != tuple([b[0],b[1]]):
									map.units[b[0]][b[1]] = map.units[c[0]][c[1]]
									map.units[c[0]][c[1]] = None
								cursor = (b[0],b[1])
								os.system('cls' if os.name == 'nt' else 'clear')
								printMap()
							else:
								#moveAction(map)
								return 0
						else:
							print "That space is unreachable."
						c = raw_input("Where should it move?: ")

				else:
					print "That selection is invalid."
				b = raw_input("Where are you selecting?: ")
		else:
			print "No nonsense, please."
		printMap()
		a = raw_input("Type a command, ? for help: ")




def actionAction(map,cursor, unit):
	""" Author: Bill Clark
	Purpose: This is the action selection chain of processing. There are more options in this area than the movement.
	if a unit that isn't friendly is nearby, attack is enabled. else, you may only call up the inventory or wait.
	in additon, as this is a bare bones ui, you can see a unit's status printout from a command here.
	This structure is almost identical to movement action. However, rather than a pile of checks, this just
	calls submethods that do stuff.
	When wait is entered, the unit is disabled for the rest of the turn, and a new call to moveaction is made.
	Booyah recursion!!!
	"""
	can_attack = False
	can_invent = True
	if map.in_prox(cursor, 'unit', unit.currRange):
		can_attack = True
	a = raw_input("Type a unit action, ? for help: ")
	while a != 'wait':
		if a == '?':
			print "select an action."
			if map.in_prox(cursor, 'unit', unit.currRange):
				can_attack = True
			print "you can: attack: " + repr(can_attack) + ' inventory: ' + repr(can_invent) + " Status: True wait: True."
		elif a == 'attack':
			if attackAction(map, cursor, unit):
				break
		elif a == 'inventory':
			inventoryAction(unit)
		elif a == 'status':
			print unit.printout()
		elif a == 'back':
			if a == 'back':
				return 1
		else:
			print "Invalid command"
		a = raw_input("Type an unit action, ? for help: ")
	unit.grey = True
	moveAction(map)
	return 0

def attackAction(map, cursor, unit):
	"""Author: Bill Clark
	Purpose: Lets a player attack an enemy unit. First a location is specificed, then, if that checks out,
			a forecast calculated. The user may then choose to complete the attack, or cancel and back out.
			The forecast, it's calculations, and the play out of that scenario are done by CombatCalc.
			Of note, after a unit attacks it may not do another action this turn.
	"""
	range = unit.currRange
	a = raw_input("Where do you want to attack?: ")
	while a != 'back':
		a = a.split(' ')
		#switches x and y to match y x format in the code. minus one is to accommodate front end non zero indexs.
		cat = a[0]
		a[0] = int(a[1])-1
		a[1] = int(cat)-1
		if (a[0],a[1]) in map.proximity(cursor, 'unit', range):
			if map.units[a[0]][a[1]] != None and map.units[a[0]][a[1]] not in map.playerArmy.units:
				forecast = CombatCalc.calc(unit, map.units[a[0]][a[1]], map.grid[cursor[0]][cursor[1]], map.grid[a[0]][a[1]])
				print forecast.readout()
				b = raw_input("Do you want to attack?: ")
				while b != 'back':
					if b == 'yes':
						forecast.play(unit, map.units[a[0]][a[1]])
						return 1
					else:
						print 'yes or no. come on genius.'
					b = raw_input("Do you want to attack?: ")
		else:
			print "can't hit it."
		a = raw_input("Where do you want to attack?: ")

#Displays the inventory. Same while loop structure as movement action. commands consist of back or equip.
def inventoryAction(unit):
	"""Author: Bill Clark
	Purpose: Lets the user interface the inventory. Barely functions, no input checking. Lets a unit equip
	        a weapon it has at the moment. Best not poked at. Weapons come pre equipped, so this isn't used atm.
	"""
	a = ''
	while a != 'back':
		os.system('cls' if os.name == 'nt' else 'clear')
		number = unit.inventory.size
		indicator = [i for i in range(1,number+1)]
		for x in range(0,number):
			print '{0:3d}. {1}'.format(indicator[x], unit.inventory.container[x])
		a = raw_input("What would you like to do?: ")
		if a == 'equip':
			b = raw_input("What Item?: ")
			while b != 'back':
				if int(b) <= number:
					if unit.ask_equippible(unit.inventory.container[int(b)-1]):
						unit.equip(int(b)-1)
						duck = raw_input("Equipped.")
						break
					else:
						duck = raw_input("Unequippible.")
				else:
					print "funny."
				b = raw_input("What Item?: ")
		elif a == 'back':
			pass
		else:
			print "Invalid."

def preBattle_Begin():
	"""There be dragons here."""
	pass

#The method that organizes the player and AI functions.
def battle_Begin():
	"""Author: Bill Clark
	Purpose: Starts the battle cycle. Player turn, Ai turn, etc.
	"""
	global turnStack
	turnStack.append(gameMap.playerArmy)
	turnStack.extend(gameMap.otherArmies)
	turn_number = 1
	while 1:
		playerTurn(turnStack[0])
		turnStack = shift(turnStack)
		AITurn(turnStack[0])
		turnStack = shift(turnStack)

#Does the players actions sequentally. Also manages turn based book keeping.
def playerTurn(army):
	"""Author: Bill Clark
	Purpose: Does the functions on a player's turn. Would have more detail if more functions were implemented.
			Right now,
	"""
	resetTempStats(army.units)
	deGray(army.units)
	moveAction(gameMap)
	print 'Player turn done'
	
#AI turn
#Checks all units that are in proximity to AI's unit and scores attacking from different
#squares that are adjacent to the target
def AITurn(army):
	"""Author: Bill Clark and Greg Suner,
	Purpose: The computer controlled units are given actions that match the AI's priorities.
	"""

	#Bookkeeping methods.
	resetTempStats(army.units)
	deGray(army.units)

	#Generates the locations of all units controlled by the Ai.
	unitLocations = []
	for row in range(len(gameMap.grid)):
		for column in range(len(gameMap.grid[row])):
			if gameMap.units[row][column] in army.units:
				unitLocations.append([row, column])

	#for each of the AI's units, looping through their locations.
	for spot in unitLocations:
		unit = gameMap.units[spot[0]][spot[1]]
		choices = {}
		if gameMap.in_prox(spot, "players", unit.ask_stat('mov')):  #If there is an enemy in range.

			#For each unit that this unit can attack.
			for foe in gameMap.proximity(spot, 'players', unit.ask_stat('mov')):

				#For each square that, using the range of the current weapon, an attack could take place from.
				for pos in gameMap.squares(foe[0], foe[1], unit.equipped.range):
					if gameMap.is_reachable(unit, tuple(spot), tuple(pos)):  #If it's actually accessable.
						#Generate a forecast, then a heuristic about it. Then store it away to be chosen later.
						forecast = CombatCalc.calc(unit, gameMap.units[foe[0]][foe[1]], gameMap.grid[pos[0]][pos[1]], \
							gameMap.grid[foe[0]][foe[1]])
						x = CombatCalc.score(unit, gameMap.units[foe[0]][foe[1]], forecast, gameMap.persona)
						choices[x] = [pos, forecast, foe]
			#make a choice
			if test: print choices
			x = choices.keys()
			x.sort()
			x = x.pop(-1)

			#move unit to the best postion to attack from and do the attack forecast.
			if choices[x][0][0] != spot[0] or choices[x][0][1] != spot[1]:
				gameMap.units[choices[x][0][0]][choices[x][0][1]] = gameMap.units[spot[0]][spot[1]]
				gameMap.units[spot[0]][spot[1]] = None
			choices[x][1].play(unit, gameMap.units[choices[x][2][0]][choices[x][2][1]])
			raw_input()  #Pause to let the user read the results.

		#If a unit isn't in range of this unit, it won't make an action. This is behavior from the source game.
		else:
			#if no unit can be reached.
			pass
	printMap()


"""Runs the program if the UI is ran. Loads specific example files, because we have no others."""
if __name__ == "__main__":
	if len(sys.argv) == 3:
		print >> sys.stderr, "Invalid number of arguments. Specify Map file, Map data, and player file."
		sys.exit()
	else:
		#gameMap = Map(*sys.argv)
		gameMap = Map('Trial_Map_Map.json','Trial_Map.json','first_army.pckl')
		os.system('cls' if os.name == 'nt' else 'clear')
		printMap()
		if gameMap.preBattle:
			preBattle_Begin()
			battle_Begin()
		else:
			battle_Begin()

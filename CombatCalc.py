from random import randint
test = False

class Forecast(object):
	"""Author: Bill Clark
		Purpose: A sub object that can calculate a combat scenario and be returned.
		The object can then be executed to have the scenario applied.
	"""

	def __init__(self):
		#Constructor.
		self.stack = []
		self.oneStats = []
		self.twoStats = []

	def play(self, unit1, unit2):
		"""Plays through the combat stack stored in the forecast. For each of the stack entries,
			rolls to hit via rand module, then critical chance in the same. Based on those booleans,
			damage is or is not assigned.
		"""
		if test: print unit1, unit2, self.stack

		for x in self.stack:
			if x[3] is unit1:  #Makes sure that the calculated values are for the given units.
				bhit = False
				bcrit = False
				dam = 0
				hit = x[1]
				if x[1] > 100:
					hit = 100
				roll = randint(1,101)  #Includes the lowest value, excludes the highest. Hence 101 for 1 to 100.

				if roll <= hit:  #No further calculations are needed if there is a miss.
					bhit = True
					crit = x[2]
					roll = randint(1,101)

					if roll <= crit:  #Damage is tripled if it's a critical. Else it is as written.
						bcrit = True
						dam = x[0] * 3
					else:
						dam = x[0]

					unit2.currentHp -= dam  #Apply damage.

				#Prints out the effects of the combat for the player.
				print unit1.personal.name, "Hit: ", repr(bhit), 'Crit: ', repr(bcrit), 'for Damage: ', repr(dam)
				print unit1.personal.name, unit1.currentHp, unit2.personal.name, unit2.currentHp

			elif x[3] is unit2:  #Makes sure that the calculated values are for the given units.
				bhit = False
				bcrit = False
				dam = 0
				hit = x[1]
				if x[1] > 100:
					hit = 100
				roll = randint(1,101)   #Includes the lowest value, excludes the highest. Hence 101 for 1 to 100.

				if roll <= hit:  #No further calculations are needed if there is a miss.
					bhit = True
					crit = x[2]
					roll = randint(1,101)

					if roll <= crit:   #Damage is tripled if it's a critical. Else it is as written.
						bcrit = True
						dam = x[0] * 3
					else:
						dam = x[0]

					unit1.currentHp -= dam #Apply damage.

				#Prints out the effects of the combat for the player.
				print unit2.personal.name, "Hit: ", repr(bhit), 'Crit: ', repr(bcrit), 'for Damage: ', repr(dam)
				print unit1.personal.name, unit1.currentHp, unit2.personal.name, unit2.currentHp
			else:
				#Something went very wrong here.
				print "shine, baka"
	def readout(self):
		"""Simple printout method for the forecast."""
		print '{0} {1} {2} {3}'.format('dam', 'hit', 'crt', 'Hp')
		for x in self.stack:
			#print x
			print '{0:3d} {1:3d} {2:3d} {3:2d} {4}'.format(x[0], x[1], x[2], x[3].currentHp, x[3].personal.name)

def calc(unit1, unit2, terrain1, terrain2):
	"""Author: Bill Clark
		Purpose:The actual calculator functionality of the class. Much is missing in the sense of this being a bare bones
		copy of the true game. However, it does contain all the functionality the game currently supports.
		Return: A forecast.
	"""

	#Look for pre combat calculation conditions.

	#Get each units gross combat relevant stats.
	oneProp = unit1.properties()
	twoProp = unit2.properties()

	#The first units actual combat stack entry.
	oneStats = [0,0,0, unit1]
	oneStats[0] += oneProp[0] - unit2.ask_stat('def') - terrain2.defen #+Triangle
	oneStats[1] += oneProp[1] - twoProp[3] - terrain2.hit #+triangle
	oneStats[2] += oneProp[2] - unit2.ask_stat('luck')

	#The second units actual combat stack entry.
	twoStats = [0,0,0, unit2]
	twoStats[0] += twoProp[0] + - unit1.ask_stat('def') - terrain1.defen #+Triangle
	twoStats[1] += twoProp[1] - oneProp[3] - terrain1.hit #+triangle
	twoStats[2] += twoProp[2] - unit1.ask_stat('luck')

	stack = []

	#If a unit's speed is higher than the other's by 5, it gets to attack twice. The number of attacks
	#are entered into the stack for the forecast.
	if unit1.ask_stat('spd') - unit2.ask_stat('spd') >= 5:
		stack.append(oneStats)
		stack.append(twoStats)
		stack.append(oneStats)
	elif unit2.ask_stat('spd') - unit1.ask_stat('spd') >= 5:
		stack.append(oneStats)
		stack.append(twoStats)
		stack.append(twoStats)
	else:
		stack.append(oneStats)
		stack.append(twoStats)

	#return a complete forecast.
	ret = Forecast()
	ret.oneStats = oneStats
	ret.twoStats = twoStats
	ret.stack = stack
	return ret
	
def score(atkUnit, defUnit, prediction, persona):
	"""Author: Greg Suner, calculations contributed by Bill Clark
	Purpose: Calculates, based on the weights for the maps AI, the heuristic value of a combat scenario.
	Return: The heuristic evaluation of a combat scenario.
	"""
	#personality is dict with OneDamage, OneHit, OneCrit, TwoDamage, TwoHit
	totalScore = 0
	
	#calc dmg dealt based of total (damage possible/expected damage done)
	totalScore += persona['OneDamage']*int((float(prediction.oneStats[0])/float(atkUnit.properties()[0]))*100)
	#dmg taken 
	totalScore -= persona['TwoDamage']*int((float(prediction.twoStats[0])/float(defUnit.properties()[0]))*100)
	#OneHit 
	totalScore += persona['OneHit']*prediction.oneStats[1]
	#TwoHit
	totalScore -= persona['TwoHit']*prediction.twoStats[1]
	#attacking units crit
	totalScore += persona['OneCrit']*prediction.oneStats[2]
	#print totalScore, 'Score'
	return totalScore


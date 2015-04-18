from random import randint
class Forecast(object):
	def __init__(self):
		self.stack = []
		self.oneStats = []
		self.twoStats = []
	def play(self, unit1, unit2):
		#print unit1, unit2, self.stack
		for x in self.stack:
			if x[3] is unit1:
				bhit = False
				bcrit = False
				dam = 0
				hit = x[1]
				if x[1] > 100:
					hit = 100
				roll = randint(0,101)

				if roll <= hit:
					bhit = True
					crit = x[2]
					roll = randint(0,101)
					if roll <= crit:
						bcrit = True
						dam = x[0] * 3
					else:
						dam = x[0]
					unit2.currentHp -= dam
				print unit1.personal.name, "Hit: ", repr(bhit), 'Crit: ', repr(bcrit), 'for Damage: ', repr(dam)
				print unit1.currentHp, unit2.currentHp
			elif x[3] is unit2:
				bhit = False
				bcrit = False
				dam = 0
				hit = x[1]
				if x[1] > 100:
					hit = 100
				roll = randint(0,101)

				if roll <= hit:
					bhit = True
					crit = x[2]
					roll = randint(0,101)
					if roll <= crit:
						bcrit = True
						dam = x[0] * 3
					else:
						dam = x[0]
					unit1.currentHp -= dam
				print unit2.personal.name, "Hit: ", repr(bhit), 'Crit: ', repr(bcrit), 'for Damage: ', repr(dam)
				print unit1.currentHp, unit2.currentHp
			else:
				print "shine, baka"
	def readout(self):
		print '{0} {1} {2} {3}'.format('dam', 'hit', 'crt', 'Hp')
		for x in self.stack:
			#print x
			print '{0:3d} {1:3d} {2:3d} {3:2d} {4}'.format(x[0], x[1], x[2], x[3].currentHp, x[3].personal.name)

def calc(unit1, unit2, terrain1, terrain2):
	#Look for pre combat calculation conditions.

	#Crunch numbers
	oneProp = unit1.properties()
	twoProp = unit2.properties()

	#one stats
	oneStats = [0,0,0, unit1]
	oneStats[0] += oneProp[0] - unit2.ask_stat('def') - terrain2.defen #+Triangle
	oneStats[1] += oneProp[1] - twoProp[3] - terrain2.hit #+triangle
	oneStats[2] += oneProp[2] - unit2.ask_stat('luck')

	twoStats = [0,0,0, unit2]
	twoStats[0] += twoProp[0] + - unit1.ask_stat('def') - terrain1.defen #+Triangle
	twoStats[1] += twoProp[1] - oneProp[3] - terrain1.hit #+triangle
	twoStats[2] += twoProp[2] - unit1.ask_stat('luck')

	stack = []
	#findout number of attacks
	if unit1.ask_stat('spd') - unit2.ask_stat('spd') >= 5:
		stack.append(oneStats)
		stack.append(oneStats)
	else:
		stack.append(oneStats)
	if unit2.ask_stat('spd') - unit1.ask_stat('spd') >= 5:
		stack.append(twoStats)
		stack.append(twoStats)
	else:
		stack.append(twoStats)
	ret = Forecast()
	ret.oneStats = oneStats
	ret.twoStats = twoStats
	ret.stack = stack
	return ret
	
#calc score of a combat situation given 2 units, a forecast, and an ai persona containing weights	
def score(self, atkUnit, defUnit, prediction, persona):
	#personality is dict with OneDamage, OneHit, OneCrit, TwoDamage, TwoHit
	totalScore = 0
	
	#calc dmg dealt based of total (damage possible/expected damage done)
	totalScore += persona['OneDamage']*((prediction.oneStats[0]/atkUnit.properties[0])*100)
	#dmg taken 
	#OneHit 
	totalScore += persona['OneHit']*prediction.oneStats[1]
	#TwoHit
	#attaking units crit
	totalScore += persona['OneCrit']*prediction.oneStats[2]

	return totalScore
	
	
	
	

	
	
	
	

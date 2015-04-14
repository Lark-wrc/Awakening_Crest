class Forecast(object):
	def __init__(self):
		self.stack = []
		self.oneStats = []
		self.twoStats = []
	def play(self, unit1, unit2):
		pass
	def readout(self):
		print '{0} {1} {2}'.format('dam', 'hit', 'crt')
		for x in self.stack:
			#print x
			print '{0:3d} {1:3d} {2:3d} {3}'.format(x[0], x[1], x[2], x[3].personal.name)

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

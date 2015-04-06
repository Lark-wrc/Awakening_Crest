#Class that holds proficiencies for each weapon as ints
class WeaponList(object)	
	attr_accessor :sword,:lance,:axe,:bow,:anima,:dark,:light,:staff
	
	#__init__ WeaponList properties
	def __init__(self,sword, lance, axe, bow, anima, dark, light, staff)
		
		self.sword = sword
		self.lance = lance
		self.axe = axe
		self.bow = bow
		self.anima = anima
		self.dark = dark
		self.light = light
		self.staff = staff
		

import 'Weapon'
#This is the interface for bow weapons. This specifies everything those
#weapons will need.#Class written by Bill Clark
class Bow(Weapon)
	
	#Creates the properties of a weapon. Used to create any new weapon object.
	#Type may seem like it is missing, but do remember this is an interface. Type is
	#Dictated by the class. This allows for new types of weapons to be created.
	def __init__(self,rank, mt, hit, crit, range, effective, uses, worth, name, iconID)
		super(rank, mt, hit, crit, range, effective, uses, worth, name, iconID)
		
	#Instructions to be run when a weapon is set to a unit's equipped slot. 
	def on_equip(self, unit)
	
	
	#If this weapon does anything special, such as allow an extra attack or grant
	#a combat skill to it's user, this method will apply it to the stack provided.
	def combat_action(self, stack)
	
	
	#The inverse of on_equip.
	def off_equip(self, unit)
	
	
	#Returns true or false if a unit can equip this weapon. Will check itself against the
	#provided unit's class's equippible list. 
	def equippible(self, unit)
	
	
	#Returns the stat (magic or strength) to be used in the combat calculator when attacking
	#with this weapon. Allows for modularity and follows the logic of a sword knowing it's a sword.
	def relevantstat(self)
	

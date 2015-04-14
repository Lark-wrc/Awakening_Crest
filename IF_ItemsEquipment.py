#A Interface for all items in the game. Every item inherits from here.\
#Class Written by Bill Clark
class Item(object):
	
	#__init__s properities of an item. 
	def __init__(self,uses, worth, name, iconID):
		self.uses = uses
		self.worth = worth
		self.name = name
		self.iconID = iconID
		self.owner = ""
	
	#If this item does something when the use option is selected, this will
	#do that. Takes a unit as items t to affect the unit using it.
	def action(unit):
		pass
	
	#Asks if this item can be used by a particular unit. Same logic as not asking
	#a sword if it is a sword.
	def ask_usable(unit):
		pass

#This is a interface for staves. It contains the methods a staff needs to function with
#the rest of the code. It is a subclass of Item.
#Class written by Bill Clark
class Staff(Item):
	
	#Creates the properties of a weapon. Used to create any new weapon object.
	#Type may seem like it is missing, but do remember this is an interface. Type is
	#Dictated by the class. This allows for new types of weapons to be created.
	def __init__(self,rank, range, uses, worth, name, iconID):
		Item.__init__(self, uses, worth, name, iconID)
		self.rank = rank
		self.range = range
	
	#Instructions to be run when a weapon is set to a unit's equipped slot. 
	def on_equip(self, unit):
		pass
	
	#If this weapon does anything special, such as allow an extra attack or grant
	#a combat skill to it's user, this method will apply it to the stack provided.
	def combat_action(self, stack):
		pass
	
	#The inverse of on_equip.
	def off_equip(self, unit):
		pass
		
	#Returns true or false if a unit can equip this weapon. Will check itself against the
	#provided unit's class's equippible list. 
	def equippible(self, unit):
		pass
	
	#Returns the stat (magic or strength): to be used in the combat calculator when attacking
	#with this weapon. Allows for modularity and follows the logic of a sword knowing it's a sword.
	def relevantstat(self):
		pass
		
#This is a interface for all weapons. It contains the methods every weapon
#will need. It is a subclass of Item.
#Class written by Bill Clark
class Weapon(Item):
	
	#Creates the properties of a weapon. Used to create any new weapon object.
	#Type may seem like it is missing, but do remember this is an interface. Type is
	#Dictated by the class. This allows for new types of weapons to be created.
	def __init__(self, rank, mt, hit, crit, range, effective, uses, worth, name, iconID):
		Item.__init__(self, uses, worth, name, iconID)
		self.rank = rank
		self.mt = mt
		self.hit = hit
		self.crit = crit
		self.range = range
		self.effective = effective
	
	#Instructions to be run when a weapon is set to a unit's equipped slot. 
	def on_equip(self, unit):
		pass
	
	#If this weapon does anything special, such as allow an extra attack or grant
	#a combat skill to it's user, this method will apply it to the stack provided.
	def combat_action(self, stack):
		pass
	
	#The inverse of on_equip.
	def off_equip(self, unit):
		pass
	
	#Returns true or false if a unit can equip this weapon. Will check itself against the
	#provided unit's class's equippible list. 
	def equippible(self, unit):
		pass
	
	#Returns the stat (magic or strength) to be used in the combat calculator when attacking
	#with this weapon. Allows for modularity and follows the logic of a sword knowing it's a sword.
	def relevantstat(self):
		pass

#This is the interface for sword weapons. This specifies everything those
#weapons will need.
#Class written by Bill Clark
class Sword(Weapon):
	
	#Creates the properties of a weapon. Used to create any new weapon object.
	#Type may seem like it is missing, but do remember this is an interface. Type is
	#Dictated by the class. This allows for new types of weapons to be created.
	def __init__(self,rank, mt, hit, crit, range, effective, uses, worth, name, iconID):
		Weapon.__init__(self,rank, mt, hit, crit, range, effective, uses, worth, name, iconID)
	
	#Instructions to be run when a weapon is set to a unit's equipped slot. 
	def on_equip(self, unit):
		pass
	
	#If this weapon does anything special, such as allow an extra attack or grant
	#a combat skill to it's user, this method will apply it to the stack provided.
	def combat_action(self, stack):
		pass
	
	#The inverse of on_equip.
	def off_equip(self, unit):
		pass
	
	#Returns true or false if a unit can equip this weapon. Will check itself against the
	#provided unit's class's equippible list. 
	def equippible(self):
		return 'Sword'
	
	#Returns the stat (magic or strength): to be used in the combat calculator when attacking
	#with this weapon. Allows for modularity and follows the logic of a sword knowing it's a sword.
	def relevantstat(self):
		pass
	
	def triangle(self, weapon):
		#ret = 0
		#weapon.is_a?(Axe): ? ret = 1 ): ret = 0
		#weapon.is_a?(Lance): ? ret = -1 ): ret = 0
		if isinstance(weapon, Lance):
			return -1
		elif isinstance(weapon, Axe):
			return 1
		else:
			return 0
		
#This is the interface for misc, no rank weapons. This specifies everything those
#weapons will need.
#Class written by Bill Clark
class Misc(Weapon):
	
	#Creates the properties of a weapon. Used to create any new weapon object.
	#Type may seem like it is missing, but do remember this is an interface. Type is
	#Dictated by the class. This allows for new types of weapons to be created.
	def __init__(self,rank, mt, hit, crit, range, effective, uses, worth, name, iconID):
		Weapon.__init__(self, rank, mt, hit, crit, range, effective, uses, worth, name, iconID)
	
	#Instructions to be run when a weapon is set to a unit's equipped slot. 
	def on_equip(self, unit):
		pass
	
	#If this weapon does anything special, such as allow an extra attack or grant
	#a combat skill to it's user, this method will apply it to the stack provided.
	def combat_action(self, stack):
		pass
	
	#The inverse of on_equip.
	def off_equip(self, unit):
		pass
	
	#Returns true or false if a unit can equip this weapon. Will check itself against the
	#provided unit's class's equippible list. 
	def equippible(self, unit):
		pass
	
	#Returns the stat (magic or strength): to be used in the combat calculator when attacking
	#with this weapon. Allows for modularity and follows the logic of a sword knowing it's a sword.
	def relevantstat(self):
		pass

#This is the interface for lance weapons. This specifies everything those
#weapons will need.
#Class written by Bill Clark
class Lance(Weapon):
	
	#Creates the properties of a weapon. Used to create any new weapon object.
	#Type may seem like it is missing, but do remember this is an interface. Type is
	#Dictated by the class. This allows for new types of weapons to be created.
	def __init__(self, rank, mt, hit, crit, range, effective, uses, worth, name, iconID):
		Weapon.__init__(self, rank, mt, hit, crit, range, effective, uses, worth, name, iconID)
	
	#Instructions to be run when a weapon is set to a unit's equipped slot. 
	def on_equip(self, unit):
		pass
	
	#If this weapon does anything special, such as allow an extra attack or grant
	#a combat skill to it's user, this method will apply it to the stack provided.
	def combat_action(self, stack):
		pass
	
	#The inverse of on_equip.
	def off_equip(self, unit):
		pass
	
	#Returns true or false if a unit can equip this weapon. Will check itself against the
	#provided unit's class's equippible list. 
	def equippible(self):
		return "Lance"
	
	#Returns the stat (magic or strength): to be used in the combat calculator when attacking
	#with this weapon. Allows for modularity and follows the logic of a sword knowing it's a sword.
	def relevantstat(self):
		pass
	
	def triangle(self, weapon):
		if isinstance(weapon, Axe):
			return -1
		elif isinstance(weapon, Sword):
			return 1
		else:
			return 0
		
#This is the interface for bow weapons. This specifies everything those
#weapons will need.#Class written by Bill Clark
class Bow(Weapon):
	
	#Creates the properties of a weapon. Used to create any new weapon object.
	#Type may seem like it is missing, but do remember this is an interface. Type is
	#Dictated by the class. This allows for new types of weapons to be created.
	def __init__(self,rank, mt, hit, crit, range, effective, uses, worth, name, iconID):
		Weapon.__init__(self, rank, mt, hit, crit, range, effective, uses, worth, name, iconID)
		
	#Instructions to be run when a weapon is set to a unit's equipped slot. 
	def on_equip(self, unit):
		pass
	
	#If this weapon does anything special, such as allow an extra attack or grant
	#a combat skill to it's user, this method will apply it to the stack provided.
	def combat_action(self, stack):
		pass
	
	#The inverse of on_equip.
	def off_equip(self, unit):
		pass
	
	#Returns true or false if a unit can equip this weapon. Will check itself against the
	#provided unit's class's equippible list. 
	def equippible(self, unit):
		pass
	
	#Returns the stat (magic or strength): to be used in the combat calculator when attacking
	#with this weapon. Allows for modularity and follows the logic of a sword knowing it's a sword.
	def relevantstat(self):
		pass

#This is the interface for axe weapons. This specifies everything those
#weapons will need.
#Class written by Bill Clark
class Axe(Weapon):
	
	#Creates the properties of a weapon. Used to create any new weapon object.
	#Type may seem like it is missing, but do remember this is an interface. Type is
	#Dictated by the class. This allows for new types of weapons to be created.
	def __init__(self,rank, mt, hit, crit, range, effective, uses, worth, name, iconID):
		Weapon.__init__(self, rank, mt, hit, crit, range, effective, uses, worth, name, iconID)
		
	#Instructions to be run when a weapon is set to a unit's equipped slot. 
	def on_equip(self, unit):
		pass
	
	#If this weapon does anything special, such as allow an extra attack or grant
	#a combat skill to it's user, this method will apply it to the stack provided.
	def combat_action(self, stack):
		pass
	
	#The inverse of on_equip.
	def off_equip(self, unit):
		pass
	
	#Returns true or false if a unit can equip this weapon. Will check itself against the
	#provided unit's class's equippible list. 
	def equippible(self):
		return "Axe"
	
	#Returns the stat (magic or strength): to be used in the combat calculator when attacking
	#with this weapon. Allows for modularity and follows the logic of a sword knowing it's a sword.
	def relevantstat(self):
		pass
	
	def triangle(self, weapon):
		if isinstance(weapon, Sword):
			return -1
		elif isinstance(weapon, Lance):
			return 1
		else:
			return 0

#This is the interface for tome weapons. This specifies everything those
#weapons will need.
#Class written by Bill Clark
class Anima(Weapon):
	
	#Creates the properties of a weapon. Used to create any new weapon object.
	#Type may seem like it is missing, but do remember this is an interface. Type is
	#Dictated by the class. This allows for new types of weapons to be created.
	def __init__(self,rank, mt, hit, crit, range, effective, uses, worth, name, iconID):
		Weapon.__init__(self, rank, mt, hit, crit, range, effective, uses, worth, name, iconID)
	
	#Instructions to be run when a weapon is set to a unit's equipped slot. 
	def on_equip(self, unit):
		pass
	
	#If this weapon does anything special, such as allow an extra attack or grant
	#a combat skill to it's user, this method will apply it to the stack provided.
	def combat_action(self, stack):
		pass
	
	#The inverse of on_equip.
	def off_equip(self, unit):
		pass
	
	#Returns true or false if a unit can equip this weapon. Will check itself against the
	#provided unit's class's equippible list. 
	def equippible(self, unit):
		pass
	
	#Returns the stat (magic or strength): to be used in the combat calculator when attacking
	#with this weapon. Allows for modularity and follows the logic of a sword knowing it's a sword.
	def relevantstat(self):
		pass

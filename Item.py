#A Interface for all items in the game. Every item inherits from here.\
#Class Written by Bill Clark
class Item 
	
	#__init__s properities of an item. 
	def __init__(self,uses, worth, name, iconID)
		self.uses = uses
		self.worth = worth
		self.name = name
		self.iconID = iconID
		self.owner = ""
	
	#If this item does something when the use option is selected, this will
	#do that. Takes a unit as items t to affect the unit using it.
	def action(unit)
	
	
	#Asks if this item can be used by a particular unit. Same logic as not asking
	#a sword if it is a sword.
	def ask_usable(unit)
	

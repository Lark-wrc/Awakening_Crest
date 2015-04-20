class Army(object):
	"""Author: Bill Clark
		Purpose: Holds all information about an army. Most of the non unit list functionality is for the player armies.
		        A container class.
	"""
	def __init__(self, units, player_name, convoy):
		self.units = units
		self.player_name = player_name
		self.convoy = convoy
	
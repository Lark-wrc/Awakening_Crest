class Inventory(object):
	"""Author: Bill Clark
		Purpose: Technically used, but basically not implemented. Manages a collection of items.
				Very little inventory management exists in this implementation of the game,
				so the effect of the this class is minimal.
	"""
	def __init__(self, size):
		self.size = size
		self.container = []
		if size != -1:
			self.container = [None for i in range(0,size)]
	def has(self, item_type):
		pass
	def trade(self, invent):
		pass
	def put(self, obj):
		if None not in self.container and len(self.container) == self.size:
			return False
		else:
			for i in range(0,self.size):
				if self.container[i] is None:
					self.container[i] = obj
					break
		
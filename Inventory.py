class Inventory(object):
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
		if len(self.container) == self.size:
			return False
		else:
			for i in range(0,size):
				if self.container[i] is None:
					self.container[i] = obj
		
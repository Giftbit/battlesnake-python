class Coordinate(object):
	x = None
	y = None

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "%s,%s" % (self.x, self.y)
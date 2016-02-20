from Coordinate import Coordinate 

class Snake(object):
	name = None
	id = None
	coords = None
	health = None

	def __init__(self, params):
		self.name = params['name']
		self.id = params['id']
		self.coords = [Coordinate(coord[0], coord[1]) for coord in params['coords']]
		self.health = params['health']

from Snake import Snake



class Game(object):

    snakeID = "34a958a3-8354-4918-995e-f6e1dede2d77"

    width = None
    height = None
    food = None
    # gold = None
    # walls = None
    snakes = None

    board = None

    mySnake = None

    def __init__(self, width, height, food, snakes):
    	self.width = width
    	self.height = height
    	self.food = food
    	self.snakes = snakes

        self.board = [[BoardType.EMPTY for x in range(height)] for y in range(width)] 

        self.populateSnakes()
        self.populateFood()

        self.findMySnake()

    def findDirection(self):
        [direction for direction in DirectionEnum.DIRECTIONS if self.isPassableDirection(direction)][0]

    def isPassableDirection(self,direction):
        return self.isPassableCoordinate( DirectionEnum.coordinate(direction, self.mySnake.coords[0] ) ) 
    

    def isValidCoordinate(self,coord):
        if (coord.x < 0 or coord.x >= self.width):
            return false
        if (cord.y < 0 or coord.y >= self.height):
            return false
        return true

    def isPassableCoordinate(self,coord):
        if not self.isValidCoordinate(coord):
            return false
        if self.board[coord.x][coord.y] != BoardType.SNAKE:
            return true
        return false


    def findMySnake(self):
        [ snake for snake in self.snakes if snake.id == Game.snakeID ][0]

    def populateSnakes(self):

        [ [self.setSquare(body.x,body.y, BoardType.SNAKE) for body in snake.coords] for snake in self.snakes ]

    def populateFood(self):

        [self.setSquare(apple.x,apple.y, BoardType.FOOD) for apple in self.food]

    def __str__(self):
        return '\n'.join([ ', '.join(row) for row in self.board])

    def setSquare(self, x, y, type):
        self.board[x][y] = type

class BoardType(object):
    EMPTY = "EMPTY"
    SNAKE = "SNAKE"
    FOOD = "FOOD!"

class DirectionEnum(object):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"

    DIRECTIONS = [NORTH, SOUTH, EAST, WEST]

    @staticmethod
    def coordinate(direction, coordinate):
        if ( direction == DirectionEnum.NORTH ) :
            return Coordinate(coordinate.x,coordinate.y-1)
        elif ( direction == DirectionEnum.SOUTH ) :
            Coordinate(coordinate.x,coordinate.y+1)
        elif ( direction == DirectionEnum.EAST ) :
            Coordinate(coordinate.x+1,coordinate.y)
        elif ( direction == DirectionEnum.WEST ) :
            Coordinate(coordinate.x-1,coordinate.y)
        


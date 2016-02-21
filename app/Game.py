from Snake import Snake
from Coordinate import Coordinate



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

        self.mySnake = self.findMySnake()

        print self.mySnake
        print self.mySnake.coords[0]
        print "end init"

    def findDirection(self):

        firstNode = Node()

        longestPath = 1
        longestDirection = "north"

        stack = []

        for direction in [direction for direction in DirectionEnum.DIRECTIONS if self.isPassableDirection(direction, self.mySnake.coords[0])]:
            node = Node()
            node.coord = DirectionEnum.coordinate(direction, self.mySnake.coords[0] )
            node.direction = direction
            node.length = 1
            stack.append(node)

        while ( len(stack) > 0  and longestPath < len(self.mySnake.coords)):
            aNode = stack.pop() 

            self.setSquare(aNode.x, aNode.y, BoardType.SNAKE)

            if ( longestPath > node.length):
                longestDirection = node.direction
                longestPath = node.length

            for direction in [direction for direction in DirectionEnum.DIRECTIONS if self.isPassableDirection(direction, aNode.coord)]:
                newNode = Node()
                newNode.coord = DirectionEnum.coordinate(direction, aNode.coord )
                newNode.direction = direction
                newNode.length = aNode.length + 1
                stack.append(newNode)


        return longestDirection



        


    def getAllPassible(self):
        return [direction for direction in DirectionEnum.DIRECTIONS if self.isPassableDirection(direction)]

    def isPassableDirection(self,direction, coord):
        return self.isPassableCoordinate( DirectionEnum.coordinate(direction, coord ) ) 
    

    def isValidCoordinate(self,coord):
        if (coord.x < 0 or coord.x >= self.width):
            return False
        if (coord.y < 0 or coord.y >= self.height):
            return False
        return True

    def isPassableCoordinate(self,coord):
        if not self.isValidCoordinate(coord): 
            return False
        if self.board[coord.x][coord.y] != BoardType.SNAKE:
            return True
        return False


    def findMySnake(self):
        return [ snake for snake in self.snakes if snake.id == Game.snakeID ][0]

    def populateSnakes(self):

        [ [self.setSquare(body.x,body.y, BoardType.SNAKE) for body in snake.coords] for snake in self.snakes ]

    def populateFood(self):

        [self.setSquare(apple.x,apple.y, BoardType.FOOD) for apple in self.food]

    def __str__(self):
        return '\n'.join([ ', '.join(row) for row in self.board])

    def setSquare(self, x, y, type):
        self.board[x][y] = type

class Node(object):
    coord = None


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
            return Coordinate(coordinate.x,coordinate.y+1)
        elif ( direction == DirectionEnum.EAST ) :
            return Coordinate(coordinate.x+1,coordinate.y)
        elif ( direction == DirectionEnum.WEST ) :
            return Coordinate(coordinate.x-1,coordinate.y)
        


import bottle
import os
from Game import Game
from Coordinate import Coordinate
from Snake import Snake


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        'color': '#00ff00',
        'head': head_url
    }


@bottle.post('/start')
def start():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'battlesnake-python!'
    }


@bottle.post('/move')
def move():

    data = bottle.request.json
    print data

    food = [Coordinate(coord[0], coord[1]) for coord in data['food']]
    snakes = [Snake(snakeParams) for snakeParams in data['snakes']]
    game = Game(data['width'], data['height'], food, snakes)
    for item in food:
        print item
    print food
    print snakes
    print game
    # TODO: Do things with data

    return {
        'move': 'north',
        'taunt': 'battlesnake-python!',
        # 'game': data.food
    }


@bottle.post('/end')
def end():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'battlesnake-python!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))

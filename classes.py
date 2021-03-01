class player:
    def __init__(self):
        self.name = ''
        self.won = False
        self.location = 'a2'
myPlayer = player()


class Enemy:
    def __init__(status):
        status.live = 'alive'


class Captain(Enemy):
    def __init__(status):
        status.live = 'alive'


class Pirate(Enemy):
    def __init__(status):
        status.live = 'alive'


class MapTile:
    """ Map with x and y coordinates"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
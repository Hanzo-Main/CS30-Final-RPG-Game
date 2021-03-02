class player:
    def __init__(self):
        """player class"""
        self.location = 'a2'
myPlayer = player()


class Enemy:
    def __init__(status):
        """enemy class"""
        status.live = 'alive'
        all_dead = False


class Captain(Enemy):
    def __init__(status):
        """child enemy class pirate"""
        status.live = 'alive'


class Pirate(Enemy):
    def __init__(status):
        """child enemy class captain"""
        status.live = 'alive'


class MapTile:
    """ runs the map"""
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Entity(object):
    def __init__(self):
        self.game = None
        super(Entity, self).__init__()

    def attach_game(self, game):
        self.game = game

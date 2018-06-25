class Area(object):
    def __init__(self):
        # game holder
        self.game = None
        super(Area, self).__init__()

    def attach_game(self, game):
        self.game = game
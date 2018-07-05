class Menu(object):
    def __init__(self):
        self.game = None
        super(Menu, self).__init__()

    def attach_game(self, game):
        self.game = game

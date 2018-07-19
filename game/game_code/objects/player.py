from lib import entity
from game_code import menus


class Player(entity.Entity):

    def __init__(self):
        self.inventory = menus.Inventory()
        self.journal = menus.Journal()
        super(Player, self).__init__()

    def attach_game(self, game):
        super(Player, self).attach_game(game)
        self.inventory.attach_game(game)
        self.journal.attach_game(game)

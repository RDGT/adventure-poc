from lib import entity
from game_code.menus import Inventory, Journal


class Player(entity.Entity):

    def __init__(self):
        self.inventory = Inventory()
        self.journal = Journal()
        super(Player, self).__init__()

    def attach_game(self, game):
        super(Player, self).attach_game(game)
        self.inventory.attach_game(game)
        self.journal.attach_game(game)

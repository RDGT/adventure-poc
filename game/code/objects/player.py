import lib
import inventory
import journal


class Player(lib.entity.Entity):

    def __init__(self):
        self.inventory = inventory.Inventory()
        self.journal = journal.Journal()
        super(Player, self).__init__()

    def attach_game(self, game):
        super(Player, self).attach_game(game)
        self.inventory.attach_game(game)
        self.journal.attach_game(game)

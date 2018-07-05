from lib import menu


class Inventory(menu.Menu):

    def __init__(self):
        self.items = []
        super(Inventory, self).__init__()

    def add_item(self, item):
        self.game.interface.display('Added {} to your inventory'.format(item.name))
        self.items.append(item)

from lib import menu


class Inventory(menu.Menu):

    def __init__(self):
        self.items = []
        super(Inventory, self).__init__('Inventory')

    @property
    def menu_items(self):
        return self.items

    def add_item(self, item, display=True):
        if display:
            self.game.interface.display('Added an item to your Inventory: {}'.format(item.name))
        self.items.append(item)

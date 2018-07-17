from lib import menu
import logging

log = logging.getLogger('menus.inventory')


class Inventory(menu.Menu):

    def __init__(self):
        self.items = []
        super(Inventory, self).__init__('Inventory')

    @property
    def menu_items(self):
        return self.items

    def add_item(self, item, display=True):
        if item in self.items:
            log.warn('item to add already exists, skip adding again: item={}'.format(item))
            return
        if display:
            self.game.interface.display('* Added an item to your Inventory: {}'.format(item.name))
        self.items.append(item)

    def remove_item(self, item, display=True):
        if item not in self.items:
            log.warn('item to remove does not exist, skip removing: item={}'.format(item))
            return
        if display:
            self.game.interface.display('* Removed an item from your Inventory: {}'.format(item.name))
        self.items.remove(item)

    def has_item(self, item):
        return bool(item in self.items)

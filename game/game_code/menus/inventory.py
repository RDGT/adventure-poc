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

    def add_item(self, item):
        if item in self.items:
            log.warn('item to add already exists, skip adding again: item={}'.format(item))
            return
        log.debug('adding inventory item: item={}'.format(item.name))
        self.items.append(item)

    def remove_item(self, item):
        if item not in self.items:
            log.warn('item to remove does not exist, skip removing: item={}'.format(item))
            return
        log.debug('removing inventory item: item={}'.format(item.name))
        self.items.remove(item)

    def has_item(self, item):
        return bool(item in self.items)

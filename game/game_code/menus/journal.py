from lib import menu
import logging

log = logging.getLogger('menus.journal')


class Journal(menu.Menu):

    def __init__(self):
        self.entries = []
        super(Journal, self).__init__('Journal')

    @property
    def menu_items(self):
        return self.entries

    def add_entry(self, entry):
        if entry in self.entries:
            log.warn('entry to add already exists, skip adding again: entry={}'.format(entry))
            return
        log.debug('adding journal entry: entry={}'.format(entry.name))
        self.entries.append(entry)

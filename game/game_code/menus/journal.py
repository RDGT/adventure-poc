from lib import menu


class Journal(menu.Menu):

    def __init__(self):
        self.entries = []
        super(Journal, self).__init__('Journal')

    @property
    def menu_items(self):
        return self.entries

    def add_entry(self, entry, display=True):
        if display:
            self.game.interface.display('Added an entry to your Journal: {} '.format(entry.name))
        self.entries.append(entry)

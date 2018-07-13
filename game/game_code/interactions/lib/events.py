
class Event(object):
    """
    an event is how the game makes stuff happen, an evnt will add items to play inventory, or journal entries
    """
    def __init__(self, **kwargs):
        super(Event, self).__init__()


class AddItem(Event):
    """add an item to the inventory"""

    def __init__(self, item, **kwargs):
        self.item = item
        super(AddItem, self).__init__(**kwargs)


class UnlockJournal(Event):
    """unlock a journal entry"""

    def __init__(self, entry, **kwargs):
        self.entry = entry
        super(UnlockJournal, self).__init__(**kwargs)

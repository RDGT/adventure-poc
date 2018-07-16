import logging

log = logging.getLogger('interactions.events')


class Event(object):
    """
    an event is how the game makes stuff happen, an evnt will add items to play inventory, or journal entries
    """
    def __init__(self, **kwargs):
        super(Event, self).__init__()

    def do_event(self, game):
        raise NotImplementedError()


class AddItem(Event):
    """add an item to the inventory"""

    def __init__(self, item, **kwargs):
        self.item = item
        super(AddItem, self).__init__(**kwargs)

    def do_event(self, game):
        game.player.inventory.add_item(self.item)


class RemoveItem(Event):
    """remove an item from the inventory"""

    def __init__(self, item, **kwargs):
        self.item = item
        super(RemoveItem, self).__init__(**kwargs)

    def do_event(self, game):
        game.player.inventory.remove_item(self.item)


class UnlockJournal(Event):
    """unlock a journal entry"""

    def __init__(self, entry, **kwargs):
        self.entry = entry
        super(UnlockJournal, self).__init__(**kwargs)

    def do_event(self, game):
        game.player.journal.add_entry(self.entry)


class ConditionalUnlockJournal(Event):
    """unlocks a journal entry depending on the first condition met"""

    def __init__(self, condition_entry_tuples, **kwargs):
        self.condition_entry_tuples = condition_entry_tuples
        super(ConditionalUnlockJournal, self).__init__(**kwargs)

    def do_event(self, game):
        for condition, entry in self.condition_entry_tuples:
            if condition.check_condition(game) in (1, 0):
                game.player.journal.add_entry(entry)
                break
        else:
            log.warn('no condition met for ConditionalUnlockJournal')


class SetRoomScreen(Event):
    """sets the room to a specific screen"""

    def __init__(self, screen_key, level=None, room=None):
        self.screen_key = screen_key
        self.level = level
        self.room = room
        super(SetRoomScreen, self).__init__()

    def do_event(self, game):
        game.current_room.set_screen(self.screen_key)


class SetRoomFlag(Event):
    """sets a room flag"""

    def __init__(self, room_flag, set_to, level=None, room=None):
        self.room_flag = room_flag
        self.set_to = set_to
        self.level = level
        self.room = room
        super(SetRoomFlag, self).__init__()

    def do_event(self, game):
        game.current_room.set_flag(self.room_flag, self.set_to)


class SetRoomFlagTrue(SetRoomFlag):
    """set a room flag to True"""

    def __init__(self, room_flag, **kwargs):
        super(SetRoomFlagTrue, self).__init__(room_flag, set_to=True, **kwargs)


class SetRoomFlagFalse(SetRoomFlag):
    """set a room flag to False"""

    def __init__(self, room_flag, **kwargs):
        super(SetRoomFlagFalse, self).__init__(room_flag, set_to=False, **kwargs)

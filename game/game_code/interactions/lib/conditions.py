class ChoiceCondition(object):
    """A choice condition is a condition which enabled or disables a choice"""
    pass


class ConditionEnable(ChoiceCondition):
    """A condition which will enable the choice"""
    pass


class ConditionDisable(ChoiceCondition):
    """A condition which will enable the choice"""
    pass


class OnlyOnce(ConditionDisable):
    """a condition which will disable the choice once it has been selected once"""
    pass


class PlayerHasItem(ConditionEnable):
    """a condition which will enable a choice if the player has the specified item"""

    def __init__(self, item):
        self.item = item
        super(PlayerHasItem, self).__init__()


class GameFlag(ConditionEnable):
    """a condition which will enable the choice once the game flag is a certain value"""

    def __init__(self, game_flag, is_value):
        self.game_flag = game_flag
        self.is_value = is_value
        super(GameFlag, self).__init__()


class GameFlagTrue(GameFlag):
    """a condition which will enable the choice once the game flag is True"""

    def __init__(self, game_flag):
        super(GameFlagTrue, self).__init__(game_flag, is_value=True)


class GameFlagFalse(GameFlag):
    """a condition which will enable the choice once the game flag is False"""

    def __init__(self, game_flag):
        super(GameFlagFalse, self).__init__(game_flag, is_value=False)


class RoomFlag(ConditionEnable):
    """a condition which will enable the choice once the room flag is a certain value"""

    def __init__(self, room_flag, is_value, level=None, room=None):
        self.room_flag = room_flag
        self.is_value = is_value
        self.level = level
        self.room = room
        super(RoomFlag, self).__init__()


class RoomFlagTrue(RoomFlag):
    """a condition which will enable the choice once the room flag is True"""

    def __init__(self, room_flag, **kwargs):
        super(RoomFlagTrue, self).__init__(room_flag, is_value=True, **kwargs)


class RoomFlagFalse(RoomFlag):
    """a condition which will enable the choice once the room flag is False"""

    def __init__(self, room_flag, **kwargs):
        super(RoomFlagFalse, self).__init__(room_flag, is_value=False, **kwargs)


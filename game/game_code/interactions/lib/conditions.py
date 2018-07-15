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


class ConditionHasItem(ConditionEnable):
    """a condition which will enable a choice if the player has the specified item"""

    def __init__(self, item):
        self.item = item
        super(ConditionHasItem, self).__init__()


class RoomFlag(ConditionEnable):
    """a condition which will enable the choice once the room flag is a certain value"""

    def __init__(self, room_flag, is_value):
        self.room_flag = room_flag
        self.is_value = is_value
        super(RoomFlag, self).__init__()


class RoomFlagTrue(RoomFlag):
    """a condition which will enable the choice once the room flag is True"""

    def __init__(self, room_flag):
        super(RoomFlagTrue, self).__init__(room_flag, is_value=True)


class RoomFlagFalse(RoomFlag):
    """a condition which will enable the choice once the room flag is False"""

    def __init__(self, room_flag):
        super(RoomFlagFalse, self).__init__(room_flag, is_value=False)


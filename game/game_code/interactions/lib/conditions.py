from game_code.core import exceptions


class ChoiceCondition(object):
    """A choice condition is a condition which enabled or disables a choice"""

    def check_condition(self, game, **kwargs):
        """
        checks this condition, should return one of (-1, 0, 1)
        -1 : condition disables
        0  : condition no effect
        1  : condition enables
        :param game:
        :param kwargs:
        :return:
        """
        raise NotImplementedError()

    def to_dict(self):
        dict_obj = self.__dict__
        dict_obj['type'] = self.__class__.__name__
        return dict_obj


class OnlyOnce(ChoiceCondition):
    """a condition which will disable the choice once it has been selected once"""

    def check_condition(self, game, **kwargs):
        choice = kwargs.pop('choice')
        if choice.has_been_selected:
            return -1
        else:
            return 1


class PlayerHasItem(ChoiceCondition):
    """a condition which will enable a choice if the player has the specified item"""

    def __init__(self, item):
        self.item = item
        super(PlayerHasItem, self).__init__()

    def check_condition(self, game, **kwargs):
        if game.player.inventory.has_item(self.item):
            return 1
        else:
            return -1


class PlayerMissingItem(ChoiceCondition):
    """a condition which will enable a choice if the player is missing the specified item"""

    def __init__(self, item):
        self.item = item
        super(PlayerMissingItem, self).__init__()

    def check_condition(self, game, **kwargs):
        if game.player.inventory.has_item(self.item):
            return -1
        else:
            return 1


class GameFlag(ChoiceCondition):
    """a condition which will enable the choice once the game flag is a certain value"""

    def __init__(self, game_flag, is_value, **kwargs):
        self.game_flag = game_flag
        self.is_value = is_value
        self.default = kwargs.pop('default', None)
        super(GameFlag, self).__init__()

    def check_condition(self, game, **kwargs):
        if game.is_flag_value(self.game_flag, self.is_value):
            return 1
        else:
            return -1


class GameFlagTrue(GameFlag):
    """a condition which will enable the choice once the game flag is True"""

    def __init__(self, game_flag, **kwargs):
        super(GameFlagTrue, self).__init__(game_flag, is_value=True, **kwargs)


class GameFlagFalse(GameFlag):
    """a condition which will enable the choice once the game flag is False"""

    def __init__(self, game_flag, **kwargs):
        super(GameFlagFalse, self).__init__(game_flag, is_value=False, **kwargs)


class RoomFlag(ChoiceCondition):
    """a condition which will enable the choice once the room flag is a certain value"""

    def __init__(self, room_flag, is_value, level=None, room=None, **kwargs):
        self.room_flag = room_flag
        self.is_value = is_value
        self.default = kwargs.pop('default', None)
        self.level = level
        self.room = room
        super(RoomFlag, self).__init__()

    def check_condition(self, game, **kwargs):
        if self.level:
            if not self.room:
                raise exceptions.GameConfigurationException(
                    'can not check room flag on specific level without specifying room')
            level = game.levels.get(self.level)
        else:
            level = game.current_level
        if self.room:
            room = level.rooms.get(self.room)
        else:
            room = game.current_room
        if room.is_flag_value(self.room_flag, self.is_value):
            return 1
        else:
            return -1


class RoomFlagTrue(RoomFlag):
    """a condition which will enable the choice once the room flag is True"""

    def __init__(self, room_flag, **kwargs):
        super(RoomFlagTrue, self).__init__(room_flag, is_value=True, **kwargs)


class RoomFlagFalse(RoomFlag):
    """a condition which will enable the choice once the room flag is False"""

    def __init__(self, room_flag, **kwargs):
        super(RoomFlagFalse, self).__init__(room_flag, is_value=False, **kwargs)


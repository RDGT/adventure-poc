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
    """a condition which will disable the condition once it has been selected once"""
    pass


class Choice(object):
    """
    a choice is how the game navigates, a choice will have a key that is held on it's screen, or elsewhere
    that key will map to a choice object.
    the choice object will let the game know how to navigate;
    the simplest choice type simply returns to the previous scene
    another common choice type navigates to a new scene.
    """
    def __init__(self, text, **kwargs):
        self.text = text
        self.key = kwargs.pop('key', None)
        self.conditions = kwargs.pop('conditions', [])
        self.enabled = True
        self._times_chosen = 0
        super(Choice, self).__init__()

    @property
    def has_been_selected(self):
        return bool(self._times_chosen > 0)

    def selected(self):
        self._times_chosen += 1


class ChoiceBack(Choice):
    """returns to previous screen/scene"""
    def __init__(self, text='Go back.', **kwargs):
        super(ChoiceBack, self).__init__(text, **kwargs)


class ChoiceNext(Choice):
    """go to next screen (for dialogue/long text)"""
    def __init__(self, text='Next', **kwargs):
        super(ChoiceNext, self).__init__(text, **kwargs)


class ChoiceJournal(Choice):
    """go to Journal"""
    def __init__(self, text='Journal', **kwargs):
        super(ChoiceJournal, self).__init__(text, key='J', **kwargs)


class ChoiceInventory(Choice):
    """go to Inventory"""
    def __init__(self, text='Inventory', **kwargs):
        super(ChoiceInventory, self).__init__(text, key='I', **kwargs)


class ChoiceNavigate(Choice):
    """navigate to a new room"""
    def __init__(self, text, level, room, scene=None, **kwargs):
        self.level = level
        self.room = room
        self.scene = scene
        super(ChoiceNavigate, self).__init__(text, **kwargs)

    def __str__(self):
        return 'ChoiceNavigate(level={} room={} scene={})'.format(self.level, self.room, self.scene)


class ChoiceInspectRoom(Choice):
    """inspect something in the room"""
    def __init__(self, text, scene, **kwargs):
        self.scene = scene
        super(ChoiceInspectRoom, self).__init__(text, **kwargs)

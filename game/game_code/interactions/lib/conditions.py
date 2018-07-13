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

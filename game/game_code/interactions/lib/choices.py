
class Choice(object):
    """
    a choice is how the game navigates, a choice will have a key that is held on it's screen, or elsewhere
    that key will map to a choice object.
    the choice object will let the game know how to navigate;
    the simplest choice type simply returns to the previous scene
    another common choice type navigates to a new scene.
    """
    pass


class ChoiceBack(Choice):
    """returns to previous screen/scene"""
    pass


class ChoiceNext(Choice):
    """go to next screen (for dialogue/long text)"""
    pass


class ChoiceNavigate(Choice):
    """navigate to a new scene (screen?)"""
    def __init__(self, target_scene):
        self.target_scene = target_scene
        super(ChoiceNavigate, self).__init__()

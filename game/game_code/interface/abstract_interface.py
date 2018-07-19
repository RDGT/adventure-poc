import logging
import itertools

log = logging.getLogger('interface.abstract')


class Decision(object):

    def __init__(self, interface, prompt_id, prompt, choices, **kwargs):
        assert isinstance(interface, Interface)
        # references
        self.interface = interface
        self.prompt_id = prompt_id
        # text and choices
        self.prompt = prompt
        self.choices = choices
        # options
        self.repeat_choices_on_bad_choice = kwargs.get('repeat', True)
        # operation
        self.choice = None
        # kwargs
        self.kwargs = kwargs
        super(Decision, self).__init__()

    def set_choice(self, choice):
        self.choice = choice

    def add_choice(self, choice, choice_key=None):
        """for debugging or cheats via choice_hook"""
        raise NotImplementedError()


class Interface(object):

    decision_class = Decision

    def __init__(self, menu_choices=None):
        self.game = None
        self.promp_id = itertools.count()
        self.menu_choices = menu_choices
        super(Interface, self).__init__()

    def attach_game(self, game):
        self.game = game

    def start(self):
        raise NotImplementedError()

    def get_next_prompt_id(self):
        return self.promp_id.next()

    def create_decision(self, prompt, choices, **kwargs):
        return self.decision_class(self, self.get_next_prompt_id(), prompt, choices, **kwargs)

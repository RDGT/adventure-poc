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

    def get_decision(self):
        self.initial_display()
        while True:
            self.prompt_for_choice()
            if self.choice:
                return self.choice
            self.show_choices()

    def initial_display(self):
        self.interface.display(self.prompt)
        self.interface.display_please_select(self)

    def show_choices(self):
        if self.repeat_choices_on_bad_choice:
            self.interface.display_choices(self)

    def prompt_for_choice(self):
        choice = self.interface.get_choice_from_player(self)
        if self.interface.is_valid_choice(self, choice):
            self.set_choice(choice)

    def set_choice(self, choice):
        self.choice = choice


class Interface(object):

    decision_class = Decision

    def __init__(self):
        self.promp_id = itertools.count()
        super(Interface, self).__init__()

    def get_next_prompt_id(self):
        return self.promp_id.next()

    @staticmethod
    def display(text):
        raise NotImplementedError()

    def display_invalid_choice(self, decision):
        raise NotImplementedError()

    def display_please_select(self, decision):
        raise NotImplementedError()

    def display_choices(self, decision):
        raise NotImplementedError()

    def prompt_for_choice(self, prompt, choices, **kwargs):
        prompt_id = self.get_next_prompt_id()
        log.debug('pfc - start: id={} prompt={} choices={} kwargs={}'.format(prompt_id, prompt, choices, kwargs))
        decision = self.decision_class(self, prompt_id, prompt, choices, **kwargs)
        choice = decision.get_decision()
        log.debug('pfc - finish: id={} choice={}'.format(prompt_id, choice))
        return choice

    def get_choice_from_player(self, decision):
        raise NotImplementedError()

    def is_valid_choice(self, decision, choice):
        raise NotImplementedError()

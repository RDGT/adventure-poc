import abstract_interface
import logging

log = logging.getLogger('interface.terminal')


class TerminalDecision(abstract_interface.Decision):

    def __init__(self, interface, decision_id, prompt, choices, **kwargs):
        choice_map, choice_display = interface.format_choices(choices, kwargs.get('by_index', True))
        self.choice_map = choice_map
        self.valid_choices = choice_map.keys() + choice_map.values()
        self.choice_display = choice_display
        super(TerminalDecision, self).__init__(interface, decision_id, prompt, choices, **kwargs)

    def set_choice(self, choice):
        self.choice = self.choice_map.get(choice, choice)


class TerminalInterface(abstract_interface.Interface):

    decision_class = TerminalDecision
    get_choice_prompt = 'Your choice?: '
    not_a_valid_choice_msg = 'Error: This is not a valid choice, choose again!'
    please_select_a_choice_msg = 'please select one of the choices:'

    @staticmethod
    def format_choices(choices, by_index=True):
        if by_index:
            choice_map = {str(i): c for i, c in enumerate(choices, start=1)}
            choice_display = '\n'.join(['- {}: {}'.format(k, v) for k, v in sorted(choice_map.items())])
        else:
            choice_map = {c: c for c in choices}
            choice_display = '\n'.join(['- {}'.format(k) for k in choice_map.keys()])
        return choice_map, choice_display

    @staticmethod
    def display(text):
        print text

    def display_invalid_choice(self, decision):
        assert isinstance(decision, TerminalDecision)
        self.display(self.not_a_valid_choice_msg)

    def display_please_select(self, decision):
        assert isinstance(decision, TerminalDecision)
        self.display(self.please_select_a_choice_msg)
        self.display_choices(decision)

    def display_choices(self, decision):
        assert isinstance(decision, TerminalDecision)
        self.display(decision.choice_display)

    def get_choice_from_player(self, decision):
        choice = raw_input(self.get_choice_prompt)
        log.debug('pfc - choice: id={} choice={}'.format(decision.prompt_id, choice))
        return choice

    def is_valid_choice(self, decision, choice):
        assert isinstance(decision, TerminalDecision)
        return bool(choice in decision.valid_choices)

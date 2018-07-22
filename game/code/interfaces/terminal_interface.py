import abstract_interface
import logging

log = logging.getLogger('interface.terminal')


class TerminalDecision(abstract_interface.Decision):

    def __init__(self, interface, decision_id, prompt, choices, **kwargs):
        assert isinstance(interface, TerminalInterface)
        choice_map, choice_display = interface.format_choices(
            choices,
            kwargs.get('add_menu_choices', True),
            kwargs.get('add_menu_exit', False),
        )
        self.choice_map = choice_map
        self.choice_display = choice_display
        super(TerminalDecision, self).__init__(interface, decision_id, prompt, choices, **kwargs)

    def initial_display(self):
        self.interface.display(self.prompt)
        self.interface.display_please_select(self)

    def show_choices(self):
        if self.repeat_choices_on_bad_choice:
            self.interface.display_choices(self)

    def prompt_for_choice(self):
        choice = self.interface.get_choice_from_player(self)
        if self.is_valid_choice(choice):
            self.set_choice(choice)

    def get_decision(self):
        self.initial_display()
        while True:
            self.prompt_for_choice()
            if self.choice:
                return self.choice
            log.debug('no valid choice selected yet')
            self.show_choices()

    def is_valid_choice(self, choice):
        valid = bool(choice in self.valid_choices)
        if valid:
            return True
        elif choice.isalpha():
            if choice.isupper():
                return bool(choice.lower() in self.valid_choices)
            else:
                return bool(choice.upper() in self.valid_choices)
        else:
            return False

    @property
    def valid_choices(self):
        return self.choice_map.keys()

    def set_choice(self, choice):
        import game.code.core.exceptions as exceptions
        self.interface.display_white_space()
        choice_obj = self.choice_map.get(choice, None)
        if choice_obj is None and choice.isalpha():
            if choice.isupper():
                choice_obj = self.choice_map.get(choice.lower(), None)
            else:
                choice_obj = self.choice_map.get(choice.upper(), None)
        if choice_obj is None:
            raise exceptions.GameInvalidChoice(choice)
        self.choice = choice_obj

    def add_choice(self, choice, choice_key=None):
        """for debugging or cheats via choice_hook"""
        choice_key = choice_key or choice.key or choice.text
        self.choice_map[choice_key] = choice


class TerminalInterface(abstract_interface.Interface):

    decision_class = TerminalDecision
    get_choice_prompt = 'Your choice?: '
    not_a_valid_choice_msg = 'Error: This is not a valid choice, choose again!'
    please_select_a_choice_msg = 'please select one of the choices:'

    def format_choices(self, choices, add_menu_choices=True, add_menu_exit=False):
        import game.code.interactions as interactions
        index = 1
        choice_map = {}
        choice_display_lines = []
        for choice in choices:
            if choice.key:
                # todo: hardening so that choice key can not be a number and clash with indexed choices
                key = str(choice.key)
            else:
                key = str(index)
                index += 1
            choice_map[key] = choice
            if not choice.hidden:
                choice_display_lines.append(' - [{}] : {}'.format(key, choice.text))
        if add_menu_choices and self.menu_choices:
            choice_map.update({c.key: c for c in self.menu_choices})
            choice_display_lines.extend(self.menu_choices_display)
        elif isinstance(add_menu_exit, interactions.choices.ChoiceExitMenu):
            choice_map.update({add_menu_exit.key: add_menu_exit})
            choice_display_lines.append(add_menu_exit.text)
        choice_display = '\n'.join(choice_display_lines)
        return choice_map, choice_display

    def __init__(self, menu_choices=None, choice_hook=False):
        if menu_choices:
            self.menu_choices_display = ['Menu Choices: {}'.format(
                ', '.join(['[{}] {}'.format(c.key, c.text) for c in menu_choices]))]
        self.choice_hook = choice_hook
        super(TerminalInterface, self).__init__(menu_choices)

    def display_screen(self, screen):
        self.display('==[ {} ]=='.format(screen.title))
        self.display(screen.text + '\n')

    def display_event_results(self, event_results):
        for event_result in event_results:
            self.display('* {}'.format(event_result.text))

    def display_white_space(self):
        self.display('\n\n')

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
        if self.choice_hook and callable(self.choice_hook):
            choice = self.choice_hook(choice, decision)
        return choice

    def do_screen(self, screen):
        import game.code.interactions as interactions
        self.display_screen(screen)
        event_results = self.game.do_screen(screen)
        if event_results:
            self.display_event_results(event_results)
        choice = None
        if screen.choices:
            enabled_choices = self.game.parse_choices(screen.choices)
            if enabled_choices:
                # get the choice from the choices on the screen
                choice = self.prompt_for_choice(
                    prompt=screen.prompt,
                    choices=enabled_choices,
                    **screen.kwargs
                )
        if choice is None:
            # if no choices possible, default to a "go back" choice
            choice = interactions.choices.ChoiceGoBack()
        self.game.handle_choice(choice)

    def prompt_for_choice(self, prompt, choices, **kwargs):
        decision = self.create_decision(prompt, choices, **kwargs)
        log.debug('pfc - start: id={} prompt={} choices={} kwargs={}'.format(
            decision.prompt_id, prompt, choices, kwargs))
        choice = decision.get_decision()
        log.debug('pfc - finish: id={} choice={}'.format(
            decision.prompt_id, choice))
        return choice

    def start(self):
        import game.code.core.exceptions as exceptions
        while self.game.operating:
            try:
                self.do_screen(self.game.get_state())
            except exceptions.GameRunTimeException as grte:
                log.error('Error in main game loop: grte={}'.format(grte))
                raise
        if self.game.the_end is not None:
            self.display(self.game.the_end)
            self.display_white_space()
            self.display('THE END')

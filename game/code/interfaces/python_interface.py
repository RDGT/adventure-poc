import abstract_interface
import logging
from code import interactions
from code.core import exceptions
log = logging.getLogger('interface.python')


class PythonDecision(abstract_interface.Decision):

    def __init__(self, interface, prompt_id, prompt, choices, **kwargs):
        assert isinstance(interface, PythonInterface)
        choice_map, choice_display = interface.format_choices(
            choices,
            kwargs.get('add_menu_choices', True),
            kwargs.get('add_menu_exit', False),
        )
        self.choice_map = choice_map
        self.choice_display = choice_display
        super(PythonDecision, self).__init__(interface, prompt_id, prompt, choices, **kwargs)

    @property
    def valid_choices(self):
        return self.choice_map.keys()

    def set_choice(self, choice):
        choice_obj = self.choice_map.get(choice, None)
        if choice_obj is None:
            raise exceptions.GameInvalidChoice(choice)
        self.choice = choice_obj

    def add_choice(self, choice, choice_key=None):
        """for debugging or cheats via choice_hook"""
        choice_key = choice_key or choice.key or choice.text
        self.choice_map[choice_key] = choice


class ConsumerPackage(object):

    def __init__(self, pid, title, text, prompt, choices, events):
        self.pid = pid
        self.title = title
        self.text = text
        self.prompt = prompt
        self.choices = choices
        self.events = events
        super(ConsumerPackage, self).__init__()

    def __str__(self):
        return 'ConsumerPackage(pid={} title="{}" choices={})'.format(self.pid, self.title, self.choices)

    def __repr__(self):
        return str(self)


class PythonInterface(abstract_interface.Interface):

    decision_class = PythonDecision

    def __init__(self, menu_choices=None):
        self.__current_decision = None
        self.__current_consumer_package = None
        super(PythonInterface, self).__init__(menu_choices)

    def format_choices(self, choices, add_menu_choices=True, add_menu_exit=False):
        index = 1
        choice_map = {}
        for choice in choices:
            if choice.key:
                # todo: hardening so that choice key can not be a number and clash with indexed choices
                key = str(choice.key)
            else:
                key = index
                index += 1
            choice_map[key] = choice

        if add_menu_choices and self.menu_choices:
            choice_map.update({c.key: c for c in self.menu_choices})
        elif isinstance(add_menu_exit, interactions.choices.ChoiceExitMenu):
            choice_map.update({add_menu_exit.key: add_menu_exit})

        choice_display = {key: choice.text for key, choice in choice_map.items() if not choice.hidden}
        return choice_map, choice_display

    def start(self):
        pass

    def reset_status(self):
        self.__current_decision = None
        self.__current_consumer_package = None

    def display(self, text):
        print text

    @property
    def is_in_progress(self):
        return bool(self.__current_decision or self.__current_consumer_package)

    def get_next_screen(self):
        if not self.game.operating:
            if self.game.the_end is not None:
                consumer_package = ConsumerPackage(-1, 'THE END', self.game.the_end, None, None, None)
                self.__current_consumer_package = consumer_package
            raise exceptions.GameNotOperating()
        elif not self.is_in_progress:
            screen = self.game.get_state()
            events = self.game.do_screen(screen)
            # default choices is always go back.. unless there are others
            choices = [interactions.choices.ChoiceGoBack()]
            if screen.choices:
                enabled_choices = self.game.parse_choices(screen.choices)
                if enabled_choices:
                    choices = enabled_choices
            # make a decision with the choices available
            decision = self.create_decision(
                prompt=screen.prompt,
                choices=choices,
                **screen.kwargs
            )
            self.__current_decision = decision
            # make a package to display to the consumer
            consumer_package = ConsumerPackage(
                pid=decision.prompt_id,
                title=screen.title,
                text=screen.text,
                prompt=screen.prompt,
                choices=decision.choice_display,
                events=events,
            )
            self.__current_consumer_package = consumer_package
        return self.__current_consumer_package

    def put_choice(self, choice):
        try:
            self.__current_decision.set_choice(choice)
        except exceptions.GameInvalidChoice:
            return False
        else:
            self.game.handle_choice(self.__current_decision.choice)
            self.reset_status()
            return True

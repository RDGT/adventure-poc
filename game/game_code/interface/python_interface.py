import Queue
import threading
import abstract_interface
import logging
import game_code.interactions.lib.choices
from game_code.core import exceptions

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

    def decision_thread(self):
        self.prompt_for_choice()

    def get_decision(self):
        self.interface.decision_queue.put(self.choice_display)
        t = threading.Thread(target=self.prompt_for_choice)
        t.start()
        while not self.choice:
            pass
        return self.choice

    def add_choice(self, choice, choice_key=None):
        """for debugging or cheats via choice_hook"""
        choice_key = choice_key or choice.key or choice.text
        self.choice_map[choice_key] = choice


class PythonInterface(abstract_interface.Interface):

    decision_class = PythonDecision

    def __init__(self, menu_choices=None):
        self.decision_queue = Queue.Queue()
        self.choice_queue = Queue.Queue()
        super(PythonInterface, self).__init__(menu_choices)

    def format_choices(self, choices, add_menu_choices=True, add_menu_exit=False):
        index = 1
        choice_map = {}
        for choice in choices:
            if choice.key:
                # todo: hardening so that choice key can not be a number and clash with indexed choices
                key = str(choice.key)
            else:
                key = str(index)
                index += 1
            choice_map[key] = choice

        if add_menu_choices and self.menu_choices:
            choice_map.update({c.key: c for c in self.menu_choices})
        elif isinstance(add_menu_exit, game_code.interactions.lib.choices.ChoiceExitMenu):
            choice_map.update({add_menu_exit.key: add_menu_exit})

        choice_display = {key: choice.text for key, choice in choice_map.items() if not choice.hidden}
        return choice_map, choice_display

    def display_screen(self, screen):
        pass

    def display_menu(self, menu):
        pass

    @staticmethod
    def display(text):
        pass

    def display_invalid_choice(self, decision):
        pass

    def display_please_select(self, decision):
        pass

    def display_choices(self, decision):
        pass

    def get_choice_from_player(self, decision):
        return self.choice_queue.get()

    def is_valid_choice(self, decision, choice):
        assert isinstance(decision, PythonDecision)
        return bool(choice in decision.valid_choices)

    def get_decision(self):
        return self.decision_queue.get()

    def put_choice(self, choice):
        self.choice_queue.put(choice)

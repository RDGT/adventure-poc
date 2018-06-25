import os
import logging
import objects
from interface import terminal_interface
from interactions.lib import choices
import core

log = logging.getLogger('game')


class Game(object):
    """
    main game object, holds everything.
    """

    def __init__(self):
        # components
        self.level_dir = core.levels_dir
        self.player = None
        self.interface = None
        # level holder
        self.levels = []
        # operation
        self.operating = False
        # navigation
        self.screen_history = []
        self.next_screen = None
        self.current_screen = None
        self.previous_screen = None
        super(Game, self).__init__()

    def add_player(self):
        self.player = objects.player.Player()

    def set_terminal_interface(self):
        interface = terminal_interface.TerminalInterface()
        self._set_interface(interface)

    def _set_interface(self, interface):
        self.interface = interface

    def new_screen(self, screen):
        self.screen_history.append(screen)
        self.previous_screen = self.current_screen
        self.current_screen = screen

    def do_screen(self, screen):
        self.new_screen(screen)
        self.interface.display_screen(screen)
        if screen.choices:
            # get the choice from the choices on the screen
            choice = self.handle_screen_choices(screen)
        else:
            # if no choices are set on the screen, default to a "go back" choice
            choice = choices.ChoiceBack()
        self.handle_choice(choice)

    def handle_screen_choices(self, screen):
        return self.interface.prompt_for_choice(
            prompt=screen.prompt,
            choices=screen.options.keys(),
            **screen.kwargs
        )

    def handle_choice(self, choice):
        if isinstance(choice, choices.ChoiceBack):
            self.next_screen = self.previous_screen

    def load_levels(self):
        level_dirs = sorted(filter(lambda name: name.startswith('level'), os.listdir(self.level_dir)))
        for level_name in level_dirs:
            self.load_level(level_name)

    def load_level(self, level_name):
        """
        a level will be in the level dir with the same name as the level dir, with the same class name as the level
        loads levels from python files (for now)
        """
        level_file_path = '{}.py'.format(os.path.join(self.level_dir, level_name, level_name))
        level_class = core.load_class_from_file(level_file_path, level_name)
        self.add_new_level(level_class)

    def add_new_level(self, level_class):
        level = level_class()
        level.attach_game(self)
        self.levels.append(level)

    def set_first_screen(self):
        self.next_screen = self.levels[0].get_first_scene()

    def start_game(self):
        self.operating = True
        self.set_first_screen()
        self.main_game_loop()
        self.operating = False

    def main_game_loop(self):
        while self.operating:
            try:
                self.do_game_cycle()
            except core.exceptions.GameRunTimeException as grte:
                log.error('Error in main game loop: grte={}'.format(grte))
                raise

    def do_game_cycle(self):
        self.do_screen(self.next_screen)


def start_game(*args):
    game = Game()
    game.add_player()
    game.set_terminal_interface()
    game.load_levels()
    game.start_game()

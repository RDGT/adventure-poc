import os
import logging
import objects
from interface import terminal_interface
from interactions.lib import choices
from interactions.lib import events
import interactions
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
        self.levels = {}
        # operation
        self.operating = False
        # navigation | screen
        self.screen_history = []
        self.next_screen = None
        self.current_screen = None
        self.previous_screen = None
        # navigation | scenes
        self.scene_history = []
        self.current_scene = None
        self.previous_scene = None
        # navigation | rooms
        self.room_history = []
        self.current_room = None
        self.previous_room = None
        # navigation | level
        self.level_history = []
        self.current_level = None
        self.previous_level = None
        super(Game, self).__init__()

    def add_player(self):
        self.player = objects.player.Player()
        self.player.attach_game(self)

    def set_terminal_interface(self):
        interface = terminal_interface.TerminalInterface(
            menu_choices=[choices.ChoiceInventory(), choices.ChoiceJournal()]
        )
        self._set_interface(interface)

    def _set_interface(self, interface):
        self.interface = interface

    def change_screen(self, screen):
        self.screen_history.append(screen)
        self.previous_screen = self.current_screen
        self.current_screen = screen
    
    def change_scene(self, scene):
        self.scene_history.append(scene)
        self.previous_scene = self.current_scene
        self.current_scene = scene

    def change_room(self, room):
        self.room_history.append(room)
        self.previous_room = self.current_room
        self.current_room = room

    def change_level(self, level):
        self.level_history.append(level)
        self.previous_level = self.current_level
        self.current_level = level

    def do_screen(self, screen):
        self.change_screen(screen)
        self.interface.display_screen(screen)
        self.handle_screen_events(screen)
        self.handle_screen_choices(screen)

    def handle_screen_events(self, screen):
        if not screen.events:
            return
        for event in screen.events:
            self.handle_event(event)

    def handle_event(self, event):
        log.debug('handling event: event={}'.format(event))
        if isinstance(event, events.AddItem):
            self.player.inventory.add_item(event.item)

    def parse_choices(self, choice_list):
        """parses choices, enabling or disabling choices based on conditions"""
        return_list = []
        for choice in choice_list:
            if choice.conditions:
                self.handle_choice_conditions(choice)
            if choice.enabled:
                return_list.append(choice)

        return return_list

    def handle_choice_conditions(self, choice):
        for condition in choice.conditions:
            if isinstance(condition, choices.OnlyOnce) and choice.has_been_selected:
                choice.enabled = False

    def handle_screen_choices(self, screen):
        choice = None
        if screen.choices:
            enabled_choices = self.parse_choices(screen.choices)
            if enabled_choices:
                # get the choice from the choices on the screen
                choice = self.interface.prompt_for_choice(
                    prompt=screen.prompt,
                    choices=enabled_choices,
                    **screen.kwargs
                )
        if choice is None:
            # if no choices are set on the screen, default to a "go back" choice
            choice = choices.ChoiceBack()
        self.handle_choice(choice)

    def handle_choice(self, choice):
        log.debug('handling choice: choice={}'.format(choice))
        choice.selected()
        if isinstance(choice, choices.ChoiceBack):
            self.next_screen = self.previous_screen
        elif isinstance(choice, choices.ChoiceNavigate):
            self.handle_navigate(choice)
        elif isinstance(choice, choices.ChoiceInspectRoom):
            self.handle_inspect(choice)
        elif isinstance(choice, choices.ChoiceInventory):
            log.debug('show inventory')
        elif isinstance(choice, choices.ChoiceJournal):
            log.debug('show journal')
        else:
            raise core.exceptions.GameConfigurationException('Bad Choice', choice)

    def handle_navigate(self, choice):
        log.debug('navigating: choice={}'.format(choice))
        level = self.levels.get(choice.level)
        if not level:
            raise core.exceptions.GameNavigateFailure('level does not exist', level)
        if level != self.current_level:
            self.change_level(level)
        assert isinstance(level, interactions.level.Level)
        room = level.rooms.get(choice.room)
        if not room:
            raise core.exceptions.GameNavigateFailure('room does not exist', room)
        assert isinstance(room, interactions.room.Room)
        if room != self.current_room:
            self.change_room(room)
        if choice.scene:
            scene = room.get_scene(choice.scene)
            self.change_scene(scene)
            self.next_screen = scene.get_current_screen()
        else:
            self.next_screen = room.get_first_screen()

    def handle_inspect(self, choice):
        log.debug('inspecting: choice={}'.format(choice))
        scene = self.current_room.get_scene(choice.scene)
        self.change_scene(scene)
        self.next_screen = scene.get_current_screen()

    def load_levels(self):
        # level_dirs = sorted(filter(lambda name: name.startswith('level'), os.listdir(self.level_dir)))
        level_dirs = ['level_1']  # todo: this is just for the beginning so i don't need to do it all
        for level_name in level_dirs:
            self.load_level(level_name)

    def load_level(self, level_name):
        """
        a level will be in the level dir with the same name as the level dir, with the same class name as the level
        loads levels from python files (for now)
        """
        level_file_path = '{}.py'.format(os.path.join(self.level_dir, level_name, level_name))
        level_class = core.load_class_from_file(level_file_path, level_name)
        self.add_new_level(level_name, level_class)

    def add_new_level(self, level_name, level_class):
        level = level_class()
        level.attach_game(self)
        level.load_rooms()
        self.levels[level_name] = level

    def set_opening_screen(self):
        opening_level = self.levels['level_1']
        opening_scene = opening_level.get_first_scene()
        opening_screen = opening_scene.get_first_screen()
        self.previous_level = self.current_level = opening_level
        self.previous_scene = self.current_scene = opening_scene
        self.previous_screen = self.current_screen = self.next_screen = opening_screen

    def start_game(self):
        self.set_opening_screen()
        self.operating = True
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

import os
import logging
import objects
from interface import terminal_interface
from interactions.lib import choices, conditions, events
from objects import item, entry
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
        # flag holder
        self.game_flags = {}
        # level holder
        self.levels = {}
        # operation
        self.operating = False
        # navigation | menu
        self.menu_enter_location = None
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
    
    def set_flag(self, flag, value):
        self.game_flags[flag] = value

    def is_flag_value(self, flag, value, default=None):
        if default is None and flag not in self.game_flags:
            return False
        return bool(self.game_flags.get(flag, default) == value)
    
    def add_player(self):
        self.player = objects.player.Player()
        self.player.attach_game(self)
        # starting items
        self.player.inventory.add_item(item.crossbow, display=False)
        self.player.inventory.add_item(item.holy_cross, display=False)
        self.player.inventory.add_item(item.holy_water, display=False)
        self.player.inventory.add_item(item.flammable_oil, display=False)
        # starting journal
        self.player.journal.add_entry(entry.equipped, display=False)

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
        screen.set_seen()
        self.handle_screen_events(screen)
        self.handle_screen_choices(screen)

    def do_menu(self, menu):
        menu_scene = menu.generate_menu_scene()
        self.next_screen = menu_scene.get_current_screen()

    def handle_screen_events(self, screen):
        if not screen.events:
            return
        for event in screen.events:
            self.handle_event(event)

    def handle_event(self, event):
        log.debug('handling event: event={}'.format(event))
        event.do_event(self)

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
        # if any conditions disable the choice, we should return to prevent accidental enables,
        # but if they enable it - keep going so that we could disable it if needed,
        # and that it will be enabled if it was not enabled
        condition_modifier = self.check_conditions(choice.conditions, choice=choice)
        if condition_modifier == -1:
            choice.disable_choice()
        elif condition_modifier == 0:
            pass
        elif condition_modifier == 1:
            choice.enable_choice()
        else:
            log.error('illegal modifier for condition: modifier={} condition_list={}'.format(
                condition_modifier, choice.conditions))
            raise core.exceptions.GameRunTimeException('illegal modifier for condition: {}'.format(condition_modifier))

    def check_conditions(self, condition_list, **kwargs):
        """
        checks the conditions,
        if the list of conditions contains any conditions disable, will return -1
        if the list of conditions does not require any action, will return 0
        if the list of conditions should enable, will return 1
        :param condition_list:
        :return:
        """
        modifier = 0
        for condition in condition_list:
            log.debug('handling condition: condition={}'.format(condition))
            action = condition.check_condition(self, **kwargs)
            if action == -1:
                modifier = -1
                break
            elif action == 0:
                pass
            elif action == 1:
                modifier = 1
            else:
                log.error('invalid action for condition: action={} condition={}'.format(action, condition))
                raise core.exceptions.GameRunTimeException('invalid action for condition: {}'.format(action))
        return modifier

    def handle_screen_choices(self, screen):
        choice = None
        if screen.choices:
            enabled_choices = self.parse_choices(screen.choices)
            enabled_choices.extend(self._choice_injection())
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
        choice.make_choice(self)

    def save_menu_enter_location(self):
        self.menu_enter_location = (self.current_level, self.current_room, self.current_scene, self.current_screen)

    def _choice_injection(self):
        """inject choices into choice list (for debugging or cheats)"""
        inject_choices = []

        debug_choices = [
            choices.ChoiceNavigate('level2', key='level2',
                                   level='level_2', room='grande_hall', hidden=True),
            choices.ChoiceNavigate('garg1', key='garg1',
                                   level='level_2', room='statue_room', scene='fight1', hidden=True),
        ]

        inject_choices.extend(debug_choices)

        return inject_choices

    def load_levels(self):
        # level_dirs = sorted(filter(lambda name: name.startswith('level'), os.listdir(self.level_dir)))
        level_dirs = ['level_1', 'level_2']  # todo: this is just for the beginning so i don't need to do it all
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

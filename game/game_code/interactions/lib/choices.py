from game_code import core
import logging

log = logging.getLogger('interactions.choices')


class Choice(object):
    """
    a choice is how the game navigates, a choice will have a key that is held on it's screen, or elsewhere
    that key will map to a choice object.
    the choice object will let the game know how to navigate;
    the simplest choice type simply returns to the previous scene
    another common choice type navigates to a new scene.
    """
    def __init__(self, text, **kwargs):
        self.text = text
        self.key = kwargs.pop('key', None)
        self.conditions = kwargs.pop('conditions', [])
        self.enabled = True
        self.hidden = kwargs.pop('hidden', False)  # for hidden choices (cheats or debug)
        self._times_chosen = 0
        super(Choice, self).__init__()

    @property
    def has_been_selected(self):
        return bool(self._times_chosen > 0)

    def selected(self):
        self._times_chosen += 1

    def disable_choice(self):
        self.enabled = False

    def enable_choice(self):
        self.enabled = True

    def make_choice(self, game):
        self.selected()
        self._make_choice(game)

    def _make_choice(self, game):
        raise NotImplementedError()


class ChoiceGoBack(Choice):
    """returns to previous screen/scene"""
    def __init__(self, text='Go back.', **kwargs):
        super(ChoiceGoBack, self).__init__(text, **kwargs)

    def _make_choice(self, game):
        game.next_screen = game.previous_screen


class ChoiceEnableDebugMode(Choice):
    """go to next screen (for dialogue/long text)"""
    def __init__(self, text='Debug Mode', **kwargs):
        super(ChoiceEnableDebugMode, self).__init__(text, key='debug-mode', hidden=True, **kwargs)

    def _make_choice(self, game):
        log.info('enabling debug mode, next log should be a debug log')
        logging.getLogger().setLevel(logging.DEBUG)
        log.debug('logging set to debug')
        game.set_flag('DEBUG', True)


class ChoiceMenuItem(Choice):
    """view item in menu"""
    def __init__(self, menu_item, **kwargs):
        self.menu_item = menu_item
        super(ChoiceMenuItem, self).__init__(text=menu_item.title, **kwargs)

    def __str__(self):
        return 'ChoiceMenuItem({})'.format(self.menu_item)

    def _make_choice(self, game):
        log.debug('menu item: choice={}'.format(self))
        game.next_screen = self.menu_item


class ChoiceExitMenu(Choice):
    """exists the current menu"""
    def __init__(self, text='Exit Menu', **kwargs):
        super(ChoiceExitMenu, self).__init__(text, key='X', **kwargs)

    def _make_choice(self, game):
        log.debug('exiting menu: loading={}'.format(game.menu_enter_location))
        level_, room_, scene_, screen_ = game.menu_enter_location
        game.next_screen = screen_


class ChoiceEnterMenu(Choice):
    """enters a menu"""

    def __init__(self, text, **kwargs):
        super(ChoiceEnterMenu, self).__init__(text, **kwargs)

    def _make_choice(self, game):
        game.save_menu_enter_location()
        log.debug('entering menu: saving={}'.format(game.menu_enter_location))
        game.do_menu(self.get_menu(game))

    def get_menu(self, game):
        raise NotImplementedError()


class ChoiceJournal(ChoiceEnterMenu):
    """go to Journal"""
    def __init__(self, text='Journal', **kwargs):
        super(ChoiceJournal, self).__init__(text, key='J', **kwargs)

    def get_menu(self, game):
        return game.player.journal


class ChoiceInventory(ChoiceEnterMenu):
    """go to Inventory"""
    def __init__(self, text='Inventory', **kwargs):
        super(ChoiceInventory, self).__init__(text, key='I', **kwargs)

    def get_menu(self, game):
        return game.player.inventory


class ChoiceNavigate(Choice):
    """navigate to a new room"""
    def __init__(self, text, level, room, scene=None, **kwargs):
        self.level = level
        self.room = room
        self.scene = scene
        super(ChoiceNavigate, self).__init__(text, **kwargs)

    def __str__(self):
        return 'ChoiceNavigate(level="{}" room="{}" scene="{}")'.format(self.level, self.room, self.scene)

    def _make_choice(self, game):
        log.debug('navigating: choice={}'.format(self))
        level = game.levels.get(self.level)
        if not level:
            raise core.exceptions.GameNavigateFailure('level does not exist', level)
        if level != game.current_level:
            game.change_level(level)
        room = level.rooms.get(self.room)
        if not room:
            raise core.exceptions.GameNavigateFailure('room does not exist', room)
        if room != game.current_room:
            game.change_room(room)
        if self.scene:
            scene = room.get_scene(self.scene)
            game.change_scene(scene)
            game.next_screen = scene.get_current_screen()
        else:
            game.next_screen = room.get_current_screen()


class ChoiceBackToRoom(Choice):
    """when inspecting a room Thing/Scene/etc you can use this choice to go back to the main Room screen(s)"""

    def _make_choice(self, game):
        log.debug('going back to room')
        game.next_screen = game.current_room.get_current_screen()


class ChoiceInspectRoom(Choice):
    """inspect something in the room"""
    def __init__(self, text, scene, **kwargs):
        self.scene = scene
        super(ChoiceInspectRoom, self).__init__(text, **kwargs)

    def __str__(self):
        return 'ChoiceInspectRoom(text="{}" scene="{}")'.format(self.text, self.scene)

    def _make_choice(self, game):
        log.debug('inspecting: choice={}'.format(self))
        scene = game.current_room.get_scene(self.scene)
        game.change_scene(scene)
        game.next_screen = scene.get_current_screen()


class ChoiceTheEnd(Choice):

    def __init__(self, text, **kwargs):
        self.ending_text = text
        super(ChoiceTheEnd, self).__init__(text='THE END', **kwargs)

    def _make_choice(self, game):
        game.set_the_end(self.ending_text)

import logging
import levels
import objects
from interface import terminal_interface

log = logging.getLogger('game')


class Game(object):
    """
    main game object, holds everything.
    """

    def __init__(self):
        self.player = None
        self.interface = None
        super(Game, self).__init__()

    def add_player(self):
        self.player = objects.player.Player()

    def set_interface(self, interface, **kwargs):
        self.interface = interface


def start_game(*args):
    game = Game()
    game.add_player()
    game.set_interface(terminal_interface.TerminalInterface())
    levels.test_level.start(game)

import sys
from optparse import OptionParser
import unittest
import logging
import game_code

log = logging.getLogger('test-adventure')


class TestAdventure(unittest.TestCase):
    def setUp(self):
        self.game = game_code.main.start_game(interface='python')

    def tearDown(self):
        self.game = None

    def test_simple(self):
        first_ = self.game.interface.get_decision()
        print first_
        self.assertTrue(self.game)


def main(args):
    parser = OptionParser()
    # parser.add_option()
    options, args = parser.parse_args(args)

    # do something with options and args to test the adventure
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAdventure)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

import sys
from optparse import OptionParser
import unittest
import logging
from code.tests import *
import code

log = logging.getLogger('test_adventure')


def test_functionality():
    suite = unittest.TestSuite()
    suite.addTest(TestAdventureFunctionality('test_starting_inventory_items'))
    suite.addTest(TestAdventureFunctionality('test_starting_journal_items'))
    return suite


def test_level_1_all():
    suite = unittest.TestSuite()
    suite.addTest(TestAdventureLevelOne('test_outside_slowly'))
    suite.addTest(TestAdventureLevelOne('test_entrance_hall_left'))
    suite.addTest(TestAdventureLevelOne('test_closet_room_search'))
    suite.addTest(TestAdventureLevelOne('test_closet_go_back'))
    suite.addTest(TestAdventureLevelOne('test_closet_room_leave'))
    suite.addTest(TestAdventureLevelOne('test_entrance_hall_right'))
    suite.addTest(TestAdventureLevelOne('test_kitchen_listen'))
    suite.addTest(TestAdventureLevelOne('test_kitchen_ask'))
    suite.addTest(TestAdventureLevelOne('test_kitchen_ask_ring'))
    suite.addTest(TestAdventureLevelOne('test_kitchen_leave'))
    suite.addTest(TestAdventureLevelOne('test_entrance_hall_front'))
    suite.addTest(TestAdventureLevelOne('test_living_room_hold'))
    suite.addTest(TestAdventureLevelOne('test_living_room_move'))
    suite.addTest(TestAdventureLevelOne('test_living_room_key'))
    suite.addTest(TestAdventureLevelOne('test_living_room_stairs'))
    suite.addTest(TestAdventureLevelOne('test_arrive_at_grande_hall'))
    return suite


def get_interactive_tester():
    return code.main.start_game(interface='python')


def main(args):
    parser = OptionParser()
    parser.add_option('-d', '--debug', dest='debug_mode',
                      help='enable debug mode',
                      action='store_true', default=False)
    parser.add_option('--log', dest='log',
                      help='should we log the game',
                      action='store_true', default=False)
    parser.add_option('--log-file', dest='log_file',
                      help='log to specified file location')
    options, args = parser.parse_args(args)

    if options.log:
        # do some logging
        if options.debug_mode:
            log_level = logging.DEBUG
        else:
            log_level = logging.INFO
        # initialize the logging
        logging.basicConfig(filename=options.log_file, level=log_level)

    # do something with options and args to test the adventure

    # run all tests selectively
    suite = unittest.TestSuite()
    suite.addTests(test_functionality())
    suite.addTests(test_level_1_all())
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

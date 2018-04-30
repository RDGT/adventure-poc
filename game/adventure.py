import sys
from optparse import OptionParser
import logging
import game_code

log = logging.getLogger('adventure')


class Adventure(object):

    def __init__(self, **kwargs):
        self.debug_mode = kwargs.pop('debug_mode', False)
        super(Adventure, self).__init__()

    def play(self, *args):
        log.info('starting to play the Adventure game!')
        return game_code.main.start_game(*args)


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

    # create the adventure object
    adventure = Adventure(**vars(options))
    # start playing the game and then exit when done
    return adventure.play(*args)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

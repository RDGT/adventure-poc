import sys
from optparse import OptionParser


class TestAdventure(object):
    # test the adventure
    pass


def main(args):
    parser = OptionParser()
    # parser.add_option()
    options, args = parser.parse_args(args)

    # do something with options and args to test the adventure

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

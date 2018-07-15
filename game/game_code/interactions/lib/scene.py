import os
from game_code import core


class Screen(object):
    """
    a screen is the smallest instance of the game. the game is comprised of screens.
    a scene can have multiple screens. and a room may have multiple scenes, while a level has multiple rooms.
    scenes could be a puzzle, dialogue, combat, or a thing.
    """

    def __init__(self, title, text, prompt=None, choices=None, events=None, **kwargs):
        self.title = title
        self.text = text
        self.prompt = prompt or 'What do you do?'
        self.choices = choices
        self.events = events
        self.kwargs = kwargs
        # been seen
        self.seen = False
        # choice holder
        self.choice = None
        # game holder
        self.game = None

    def set_seen(self):
        self.seen = True

    def attach_game(self, game):
        self.game = game

    def update_choice(self, choice):
        self.choice = choice

    def do_screen(self):
        self.game.do_scene(self)


class Scene(object):

    def __init__(self, name, opening_text, prompt=None, choices=None, events=None, screens=None, **kwargs):
        """
        Creates a new scene to be used in the Adventure
        :param name: the name of the scene
        :param opening_text: the text to show the user when entering the scene
        :param prompt: the prompt for choices
        :param options: a dictionary, of choices {'string_choice': next_scene_object}
        :param kwargs: kwargs to send the "prompt for choice" method
        """
        prompt = prompt or 'What do you do?'
        self.name = name
        self.kwargs = kwargs
        # game holder
        self.game = None
        self.screens = {}
        # add scene intro screen / all leftover kwargs are sent - please consume kwargs before
        self.add_screen('intro', Screen(self.name, opening_text, prompt, choices, events, **kwargs))
        if screens:
            for screen in screens:
                self.add_screen(screen.title, screen)
        # location in scene (start at intro)
        self.current_screen = 'intro'
        super(Scene, self).__init__()

    def add_screen(self, screen_key, screen_instance):
        screen_instance.attach_game(self.game)
        self.screens[screen_key] = screen_instance

    def attach_game(self, game):
        self.game = game

    def set_screen(self, screen_key):
        self.current_screen = screen_key

    def get_first_screen(self):
        return self.screens['intro']

    def get_current_screen(self):
        return self.screens[self.current_screen]


def scene_loader(path, root=None):
    """
    loads a scene from its string path relative to root
    :param path: the . seperated path of the scene to load
    :param root: the root of the dir to load, defaults to levels dir
    :return:
    """
    root = root or core.levels_dir
    # format names
    path_sections = path.split('.')
    scene_name = path_sections.pop(-1)
    library_path = '{}.py'.format(os.path.join(root, *path_sections))
    # load scene
    return core.load_class_from_file(library_path, scene_name)


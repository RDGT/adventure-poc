import os
from game_code import core


class Screen(object):
    """
    a screen is the smallest instance of the game. the game is comprised of screens.
    a scene can have multiple screens. and a room may have multiple scenes, while a level has multiple rooms.
    scenes could be a puzzle, dialogue, combat, or a thing.
    """

    def __init__(self, title, text, prompt=None, choices=None, **kwargs):
        self.title = title
        self.text = text
        self.prompt = prompt or 'What do you do?'
        self.choices = choices
        self.kwargs = kwargs
        # choice holder
        self.choice = None
        # game holder
        self.game = None

    def attach_game(self, game):
        self.game = game

    def update_choice(self, choice):
        self.choice = choice

    def do_screen(self):
        self.game.do_screen(self)


class Scene(object):

    def __init__(self, name, opening_text, prompt=None, options=None, **kwargs):
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
        self.opening_text = opening_text
        self.prompt = prompt
        self.options = options or {}
        self.kwargs = kwargs
        # game holder
        self.game = None
        super(Scene, self).__init__()

    def attach_game(self, game):
        self.game = game

    def set_options(self, options):
        """set options on a scene"""
        for key, value in options.items():
            self.set_option(key, value)

    def set_option(self, key, destination):
        self.options[key] = destination

    def run_scene(self, game):
        # todo: add documentation @inbar
        game.interface.display('==[ {} ]=='.format(self.name))
        game.interface.display(self.opening_text)
        if self.prompt and self.options:
            choice = game.interface.prompt_for_choice(self.prompt, self.options.keys(), **self.kwargs)
            next_scene = self.get_scene(self.options[choice])
            assert isinstance(next_scene, Scene)
            return next_scene.run_scene(game)

    def get_scene(self, scene):
        if isinstance(scene, Scene):
            return scene
        else:
            return scene_loader(scene)


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


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
        self.name = name
        self.opening_text = opening_text
        self.prompt = prompt
        self.options = options or {}
        self.kwargs = kwargs
        super(Scene, self).__init__()

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
            next_scene = self.options[choice]
            assert isinstance(next_scene, Scene)
            return next_scene.run_scene(game)

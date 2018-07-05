from lib import scene


class Room(scene.Scene):

    def __init__(self, name, opening_text, prompt=None, choices=None, scenes=None, **kwargs):
        self.scenes = scenes or {}
        super(Room, self).__init__(name, opening_text, prompt, choices, **kwargs)

    def add_scene(self, scene_key, scene_instance):
        self.scenes[scene_key] = scene_instance

    def get_scene(self, scene_key):
        return self.scenes[scene_key]

from lib import scene


class Room(scene.Scene):

    def __init__(self, name, opening_text, prompt=None, choices=None, scenes=None, room_flags=None, **kwargs):
        self.scenes = scenes or {}
        self.room_flags = room_flags or {}
        super(Room, self).__init__(name, opening_text, prompt, choices, **kwargs)

    def set_flag(self, flag, value):
        self.room_flags[flag] = value

    def is_flag_value(self, flag, value, default=None):
        if default is None and flag not in self.room_flags:
            return False
        return bool(self.room_flags.get(flag, default) == value)

    def add_scene(self, scene_key, scene_instance):
        self.scenes[scene_key] = scene_instance

    def get_scene(self, scene_key):
        return self.scenes[scene_key]

    def get_first_screen(self):
        return super(Room, self).get_first_screen()

    def to_dict(self):
        dict_obj = super(Room, self).to_dict()
        for scene_key, scene_obj in self.scenes.items():
            dict_obj['scenes'][scene_key] = scene_obj.to_dict()
        dict_obj['type'] = 'room'
        return dict_obj

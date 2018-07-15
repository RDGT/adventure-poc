from lib import scene


class Room(scene.Scene):

    def __init__(self, name, opening_text, prompt=None, choices=None, scenes=None, room_flags=None, **kwargs):
        self.scenes = scenes or {}
        self.room_flags = room_flags or {}
        self.future_text = kwargs.pop('future_text', False)
        super(Room, self).__init__(name, opening_text, prompt, choices, **kwargs)

    def set_flag(self, flag, value):
        self.room_flags[flag] = value

    def is_flag_value(self, flag, value):
        if flag not in self.room_flags:
            return False
        return bool(self.room_flags.get(flag) == value)

    def add_scene(self, scene_key, scene_instance):
        self.scenes[scene_key] = scene_instance

    def get_scene(self, scene_key):
        return self.scenes[scene_key]

    def get_first_screen(self):
        return super(Room, self).get_first_screen()

    def get_current_screen(self):
        if self.current_screen == 'intro' and self.screens['intro'].seen and self.future_text:
            self.screens['intro'].text = self.future_text
        return super(Room, self).get_current_screen()

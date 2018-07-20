from game_code.interactions import level
from game_code.levels.level_3 import temple_room, inner_cloister


class level_3(level.Level):

    def get_first_scene(self):
        return self.rooms['temple_room']

    def load_rooms(self):
        self.load_room('temple_room', temple_room.temple_room)
        self.load_room('inner_cloister', inner_cloister.inner_cloister)

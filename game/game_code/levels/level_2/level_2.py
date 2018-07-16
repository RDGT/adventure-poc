from game_code.interactions import level
from game_code.levels.level_2 import dining_room, grande_hall, library


class level_2(level.Level):

    def get_first_scene(self):
        return self.rooms['outside']

    def load_rooms(self):
        self.load_room('grande_hall', grande_hall.grande_hall1)
        self.load_room('dining_room', dining_room.dining_room)
        self.load_room('library', library.library)

from game_code.interactions import level
from game_code.levels.level_2 import dining_room, grande_hall, library, laboratory, bedroom


class level_2(level.BasicLevel):

    def get_first_scene(self):
        return self.rooms['grande_hall']

    def load_rooms(self):
        self.load_room('grande_hall', grande_hall.grande_hall)
        self.load_room('dining_room', dining_room.dining_room)
        self.load_room('library', library.library)
        self.load_room('laborataory', laboratory.laboratory)
        self.load_room('bedroom', bedroom.bedroom)

from game_code.interactions import level
from game_code.levels.level_1 import outside, closet_room, entrance_hall, kitchen, living_room


class level_1(level.BasicLevel):

    def get_first_scene(self):
        return self.rooms['outside']

    def load_rooms(self):
        self.load_room('outside', outside.outside)
        self.load_room('closet_room', closet_room.closet_room)
        self.load_room('entrance_hall', entrance_hall.entrance_hall)
        self.load_room('kitchen', kitchen.kitchen)
        self.load_room('living_room', living_room.living_room)


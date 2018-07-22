from game.code.interactions import level
from game.code.levels.level_1 import outside, closet_room, entrance_hall, kitchen, living_room


level_1 = level.Level(
    name='level_1',
    rooms={
        'outside': outside.outside,
        'closet_room': closet_room.closet_room,
        'entrance_hall': entrance_hall.entrance_hall,
        'kitchen': kitchen.kitchen,
        'living_room': living_room.living_room,
    }
)

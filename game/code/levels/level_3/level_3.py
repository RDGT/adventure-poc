from code.interactions import level
from code.levels.level_3 import temple_room, inner_cloister


level_3 = level.Level(
    name='level_3',
    rooms={
        'temple_room': temple_room.temple_room,
        'inner_cloister': inner_cloister.inner_cloister,
    }
)

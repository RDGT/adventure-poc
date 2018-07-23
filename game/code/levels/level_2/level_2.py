from code.interactions import level
from code.levels.level_2 import dining_room, grande_hall, library, laboratory, bedroom, statue_room

level_2 = level.Level(
    name='level_2',
    rooms={
        'grande_hall': grande_hall.grande_hall,
        'dining_room': dining_room.dining_room,
        'library': library.library,
        'laboratory': laboratory.laboratory,
        'bedroom': bedroom.bedroom,
        'statue_room': statue_room.statue_room,
    }
) 

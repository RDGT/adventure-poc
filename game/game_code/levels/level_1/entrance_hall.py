from game_code import interactions

entrance_hall = interactions.room.Room(
    name='Entrance Hall',
    opening_text='beyond the door is a circular wide room.\n'
                 'The air is moldy and the floor is covered with dust.\n'
                 'There are three doors leading away from the hall.',
    options={
        'Left door': 'level_1.closet_room.closet_room',
        'Front door': 'level_1.living_room.living_room',
        'Right door': 'level_1.kitchen.kitchen',
    }
)

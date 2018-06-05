from game_code import interactions


examine_table = interactions.scene.Scene(
    # todo: alon finish the text
    name='Table',
    opening_text='Treasure room somewhere!',
    options={
         'Go Back to the Grande Hall': 'level_2.grande_hall.grande_hall1',
    }
)


dining_room1 = interactions.room.Room(
    # todo: alon to add text
    name='Dining Room',
    opening_text='dining room',
    options={
        'Examine Table': 'level_2.grande_hall.examine_table',
        'Go Back to the Grande Hall': 'level_2.grande_hall.grande_hall1',
    }
)

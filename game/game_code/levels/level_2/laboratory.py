from game_code import interactions

chemistry_apparatus = interactions.scene.Scene(
    # todo: alon finish the text
    name='chemistry apparatus',
    opening_text='you make nitro',
    options={
         'little lockbox': 'level_2.laboratory.little_lockbox',
         'Go Back to the Grande Hall': 'level_2.grande_hall.grande_hall2',
    }
)


little_lockbox = interactions.scene.Scene(
    # todo: alon finish the text
    name='lockbox',
    opening_text='you find a gem',
    options={
         'chemistry apparatus': 'level_2.laboratory.chemistry_apparatus',
         'Go Back to the Grande Hall': 'level_2.grande_hall.grande_hall2',
    }
)


laboratory = interactions.room.Room(
    # todo: alon to add text
    name='Dining Room',
    opening_text='dining room',
    options={
        'little lockbox': 'level_2.laboratory.little_lockbox',
        'chemistry apparatus': 'level_2.laboratory.chemistry_apparatus',
        'Go Back to the Grande Hall': 'level_2.grande_hall.grande_hall2',
    }
)

from game_code import interactions


converse = interactions.scene.Scene(
    # todo: finish the text
    # todo: conditional options based on known information (journal entries)
    name='Talking to the Ghoul',
    opening_text='talk talk talk',
    options={
        'done': 'level_2.grande_hall.grande_hall2',
    }
)

butler_dead = interactions.scene.Scene(
    # todo: alon make text
    name='He is dead',
    opening_text='blah',
    options={
        'look around the room': 'level_2.grande_hall.grande_hall2',
    }
)

fight = interactions.scene.Scene(
    # todo: combat
    name='Fighting the Ghoul',
    opening_text='fight fight fight',
    options={
        'Kill it.': 'level_2.grande_hall.butler_dead',
    }
)

grande_hall2 = interactions.room.Room(
    name='Grande Hall',
    opening_text='looking around',
    options={
        'Left Room': 'level_2.dining_room.dining_room1',
        'Far Left Room': 'level_2.grande_hall.fight',
        'Right Room': 'level_2.library.library',
        'Far Right Room': 'level_2.grande_hall.fight',
    }
)

grande_hall1 = interactions.room.Room(
    name='Grande Hall',
    opening_text='ghoul butler',
    options={
        'Converse': 'level_2.grande_hall.converse',
        'Fight': 'level_2.grande_hall.fight',
    }
)

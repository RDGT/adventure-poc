from game_code import interactions


writing_desk = interactions.scene.Scene(
    # todo: alon finish the text
    name='Writing Desk',
    opening_text='Find a scribble',
    options={
         'Go Back to the Grande Hall': 'level_2.grande_hall.grande_hall1',
    }
)


library = interactions.room.Room(
    # todo: alon to add text
    name='Library',
    opening_text='lib',
    options={
        'Writing Desk': 'level_2.library.writing_desk',
        'Go Back to the Grande Hall': 'level_2.grande_hall.grande_hall1',
    }
)

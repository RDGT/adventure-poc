from game_code import interactions

outside = interactions.room.Room(
    name='Outside',
    opening_text='You are a badass holy inquisitor, here to banish evil.\n'
                 'You stand before the main entrance to the cursed dungeon where evil lurks.\n'
                 'The large wooden door before you seems old and rotten.',
    options={
        'Open the door slowly': 'level_1.entrance_hall.entrance_hall',
        'Kick down the door!': 'level_1.entrance_hall.entrance_hall',
    }
)
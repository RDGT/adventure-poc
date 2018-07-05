from game_code import interactions
from game_code.interactions.lib import choices

outside = interactions.room.Room(
    name='Outside',
    opening_text='You are a badass holy inquisitor, here to banish evil.\n'
                 'You stand before the main entrance to the cursed dungeon where evil lurks.\n'
                 'The large wooden door before you seems old and rotten.',
    choices=[
        choices.ChoiceNavigate('Open the door slowly', level='level_1', room='entrance_hall'),
        choices.ChoiceNavigate('Kick down the door!', level='level_1', room='entrance_hall'),
    ]
)

from game.code import interactions
from game.code.interactions.lib import choices, events
from game.code.objects import entry

outside = interactions.room.Room(
    name='Outside',
    opening_text='You are a bad ass holy inquisitor, here to banish evil.\n'
                 'You carry with you a crossbow, a holy cross, a vial of holy water and a vial of flammable oil.\n'
                 'Other than your wits these are your only weapons.\n'
                 'You stand before the main entrance to the cursed dungeon where evil lurks.\n'
                 'The large wooden door before you seems old and rotten',
    choices=[
        choices.ChoiceNavigate('Open the door slowly', level='level_1', room='entrance_hall'),
        choices.ChoiceNavigate('Kick down the door!', level='level_1', room='entrance_hall'),
    ],
    add_menu_choices=False,
)

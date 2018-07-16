from game_code import interactions
from game_code.interactions.lib import choices, events, conditions, scene
from game_code.objects import item, entry

statue_room = interactions.room.Room(
    name='Statue Room',
    opening_text='You go through the passage and enter an oval room filled with statues.\n'
                 'At the far end there is a large statue of a gargoyle.\n'
                 'As you approach the gargoyle, his eyes light up in green flames and he issues a warning:\n'
                 '"Only the head of the estate may pass".',
    choices=[
        choices.ChoiceInspectRoom('Present Robert\'s head', scene='head'),
        choices.ChoiceInspectRoom('Fight the Gargoyle', scene='fight2'),
        choices.ChoiceNavigate('Leave room', level='level_2', room='grande_hall'),
    ],
    screens={

    },
    scenes={
        'head': interactions.thing.Thing(
            name='Mirror',
            opening_text='Assuming the gargoyle might refer to Robert, you present the mummified head.\n'
                         'That gargoyle bows and then gets up and moves to the side,\n'
                         'revealing a stone archway and a staircase leading down.',
            choices=[
                choices.ChoiceNavigate('Descend through the stone arch', level='level_3', room='temple_room'),
                choices.ChoiceNavigate('Go back to the Grande Hall', level='level_2', room='grande_hall'),
            ],
        ),

        'fight1': interactions.thing.Thing(
            name='Gargoyle attacks!',
            opening_text='You have only a fraction of a second to respond!',
            choices=[
                choices.ChoiceNavigate('Leave room (temp)', level='level_2', room='grande_hall'),  # temp
            ],
        ),


        'fight2': interactions.combat.Combat(
            name='Combat with Gargoyle',
            opening_text='Defeating this monstrous stone construct will be no easy feat.',
            choices=[
                choices.ChoiceNavigate('Leave room (temp)', level='level_2', room='grande_hall'),  # temp
            ],
        ),

    }
)

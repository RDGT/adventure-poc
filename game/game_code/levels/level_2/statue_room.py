from game_code import interactions
from game_code.interactions.lib import choices, events, conditions, scene
from game_code.objects import item, entry

statue_room = interactions.room.Room(
    name='Statue Room',
    opening_text='You go through the passage and enter an oval room filled with statues.\n'
                 'At the far end there is a large statue of a gargoyle.\n'
                 'As you approach the gargoyle, his eyes light up in green flames and he issues a warning:\n'
                 '"Only the head of the estate may pass".',
    room_flags={'retreated': False},
    choices=[
        choices.ChoiceInspectRoom('Present Robert\'s head', scene='head'),
        choices.ChoiceInspectRoom('Fight the Gargoyle', scene='fight2'),
        choices.ChoiceNavigate('Leave room', level='level_2', room='grande_hall'),
    ],
    screens={
        'clear': scene.Screen(
            title='Statue Room',
            text='You go through the passage and enter an oval room filled with statues.\n'
                 'at the end is a stone archway and a staircase leading down.',
            choices=[
                choices.ChoiceNavigate('Descend through the stone arch', level='level_3', room='temple_room'),
                choices.ChoiceNavigate('Go back to the Grande Hall', level='level_2', room='grande_hall'),
            ],
        )
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
            events=[events.SetRoomScreen('clear')]
        ),
        # == fight 1 ==
        'fight1': interactions.combat.Combat(
            name='Gargoyle attacks!',
            opening_text='You have only a fraction of a second to respond!',
            choices=[
                choices.ChoiceInspectRoom('Use Holy Cross', scene='fight1_cross',
                                          conditions=[conditions.PlayerHasItem(item.holy_cross)]),
                choices.ChoiceInspectRoom('Shoot crossbow', scene='fight1_shoot',
                                          conditions=[conditions.PlayerHasItem(item.crossbow)]),
                choices.ChoiceInspectRoom('Use Holy Water', scene='fight1_water',
                                          conditions=[conditions.PlayerHasItem(item.holy_water)]),
                choices.ChoiceInspectRoom('Burn him with fire', scene='fight1_fire',
                                          conditions=[conditions.PlayerHasItem(item.flammable_oil)]),
                choices.ChoiceInspectRoom('Throw Nitroglycerin', scene='fight1_nitro',
                                          conditions=[conditions.PlayerHasItem(item.nitro)]),
            ],
        ),
        'fight1_cross': interactions.thing.Thing(
            name='Gargoyle attacks!',
            opening_text='You raise your cross against the gargoyle and begin to recite prayer.\n'
                         'The stone creature does not even flinch,\n'
                         'and proceeds to slam his rock arm into you in a sweeping motion.\n'
                         'The blow sends you flying back and crashing to the floor.\n'
                         'Your Holy Cross is broken!',
            choices=[
                choices.ChoiceInspectRoom('Shoot crossbow', scene='fight1_shoot',
                                          conditions=[conditions.PlayerHasItem(item.crossbow)]),
                choices.ChoiceInspectRoom('Use Holy Water', scene='fight1_water',
                                          conditions=[conditions.PlayerHasItem(item.holy_water)]),
                choices.ChoiceInspectRoom('Burn him with fire', scene='fight1_fire',
                                          conditions=[conditions.PlayerHasItem(item.flammable_oil)]),
                choices.ChoiceInspectRoom('Throw Nitroglycerin', scene='fight1_nitro',
                                          conditions=[conditions.PlayerHasItem(item.nitro)]),
                choices.ChoiceNavigate('Retreat to the Grande Hall', level='level_2', room='grande_hall',
                                       scene='gargoyle_fight')
            ],
            events=[events.RemoveItem(item.holy_cross)]
        ),
        'fight1_shoot': interactions.thing.Thing(
            name='Gargoyle attacks!',
            opening_text='Without hesitation you bring up the loaded crossbow\n'
                         'and shoot the gargoyle directly in the eye.\n'
                         'The bolt breaks against the stone eye and the gargoyles charge is unhindered.\n'
                         'With a hard stone fist he sends you flying against a wall.',
            choices=[
                choices.ChoiceInspectRoom('Use Holy Cross', scene='fight1_cross',
                                          conditions=[conditions.PlayerHasItem(item.holy_cross)]),
                choices.ChoiceInspectRoom('Use Holy Water', scene='fight1_water',
                                          conditions=[conditions.PlayerHasItem(item.holy_water)]),
                choices.ChoiceInspectRoom('Burn him with fire', scene='fight1_fire',
                                          conditions=[conditions.PlayerHasItem(item.flammable_oil)]),
                choices.ChoiceInspectRoom('Throw Nitroglycerin', scene='fight1_nitro',
                                          conditions=[conditions.PlayerHasItem(item.nitro)]),
                choices.ChoiceNavigate('Retreat to the Grande Hall', level='level_2', room='grande_hall',
                                       scene='gargoyle_fight')
            ],
            events=[events.RemoveItem(item.holy_cross)]
        ),
        'fight1_water': interactions.thing.Thing(
            name='Gargoyle attacks!',
            opening_text='You retreat to make some space between you and the monster,\n'
                         'then throw the vial of holy water. The vial breaks against the stone skin of the gargoyle\n'
                         'yet seems to have no effect. The attack continues!',
            choices=[
                choices.ChoiceInspectRoom('Use Holy Cross', scene='fight1_cross',
                                          conditions=[conditions.PlayerHasItem(item.holy_cross)]),
                choices.ChoiceInspectRoom('Shoot crossbow', scene='fight1_shoot',
                                          conditions=[conditions.PlayerHasItem(item.crossbow)]),
                choices.ChoiceInspectRoom('Burn him with fire', scene='fight1_fire',
                                          conditions=[conditions.PlayerHasItem(item.flammable_oil)]),
                choices.ChoiceInspectRoom('Throw Nitroglycerin', scene='fight1_nitro',
                                          conditions=[conditions.PlayerHasItem(item.nitro)]),
                choices.ChoiceNavigate('Retreat to the Grande Hall', level='level_2', room='grande_hall',
                                       scene='gargoyle_fight')
            ],
            events=[events.RemoveItem(item.holy_cross)]
        ),
        'fight1_fire': interactions.thing.Thing(
            name='Gargoyle attacks!',
            opening_text='You throw the oil vial at the gargoyle and dive out of the way as he charges forward.\n'
                         'You get up quickly and send a few glowing sparks from your flint.\n'
                         'The gargoyle catches fire yet does not slow down. The attack continues!',
            choices=[
                choices.ChoiceInspectRoom('Use Holy Cross', scene='fight1_cross',
                                          conditions=[conditions.PlayerHasItem(item.holy_cross)]),
                choices.ChoiceInspectRoom('Shoot crossbow', scene='fight1_shoot',
                                          conditions=[conditions.PlayerHasItem(item.crossbow)]),
                choices.ChoiceInspectRoom('Use Holy Water', scene='fight1_water',
                                          conditions=[conditions.PlayerHasItem(item.holy_water)]),
                choices.ChoiceInspectRoom('Throw Nitroglycerin', scene='fight1_nitro',
                                          conditions=[conditions.PlayerHasItem(item.nitro)]),
                choices.ChoiceNavigate('Retreat to the Grande Hall', level='level_2', room='grande_hall',
                                       scene='gargoyle_fight')
            ],
            events=[events.RemoveItem(item.holy_cross)]
        ),
        'fight1_nitro': interactions.thing.Thing(
            name='Gargoyle attacks!',
            opening_text='You toss the vial of nitroglycerin and duck for cover\n'
                         'as a large explosion sends debris in all directions.',
            choices=[
                choices.ChoiceInspectRoom('Wait for the dust to settle', scene='gargoyle_defeated'),
            ],
            events=[events.RemoveItem(item.nitro)]
        ),
        'gargoyle_defeated': interactions.thing.Thing(
            name='Gargoyle Defeated!',
            opening_text='When the dust settles, where the gargoyle once was there but a pile of rubble.\n'
                         'The path is cleared.',
            choices=[
                choices.ChoiceNavigate('Descend through the stone arch', level='level_3', room='temple_room',
                                       conditions=[conditions.RoomFlagFalse('retreated')]),
                choices.ChoiceNavigate('Go back to the Grande Hall', level='level_2', room='grande_hall',
                                       conditions=[conditions.RoomFlagFalse('retreated')]),
                choices.ChoiceBackToRoom('Back to the Statue Room', conditions=[conditions.RoomFlagTrue('retreated')]),
            ],
            events=[events.RemoveItem(item.holy_cross), events.SetRoomScreen('clear')]
        ),
        # == fight 2 ==
        'fight2': interactions.combat.Combat(
            name='Combat with Gargoyle',
            opening_text='Defeating this monstrous stone construct will be no easy feat.',
            choices=[
                choices.ChoiceNavigate('Leave room (temp)', level='level_2', room='grande_hall'),  # temp
            ],
        ),

    }
)

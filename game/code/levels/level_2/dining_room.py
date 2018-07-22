from game.code import interactions
from game.code.interactions.lib import choices, events, conditions
from game.code.objects import item, entry


dining_room = interactions.room.Room(
    name='Dining Room',
    opening_text='You enter the dining room. A long marble table runs the length of the decorated chamber.\n'
                 'Carved wooden chairs surround the table on both sides.',
    room_flags={'found_treasure': False, 'door_open': False, 'shoot': False, 'water': False},
    choices=[
        choices.ChoiceInspectRoom('Examine the Table', 'table'),
        choices.ChoiceInspectRoom('Hidden Door', 'hidden_door',
                                  conditions=[conditions.RoomFlagTrue('door_open'),
                                              conditions.RoomFlagFalse('found_treasure')]),
        choices.ChoiceNavigate('Leave room', level='level_2', room='grande_hall'),
    ],
    scenes={
        'table': interactions.thing.Thing(
            name='Table',
            opening_text='After observing the table from all sides you decide to take a look underneath.\n'
                         'You lift the silken table cloth to find an inscription carved into one of the legs\n'
                         '"Fortunes close. Masked by time"',
            future_text='The inscription carved into one of the legs reads: "Fortunes close. Masked by time"',
            events=[events.UnlockJournal(entry.examine_table)]
        ),
        'hidden_door': interactions.thing.Thing(
            name='Hidden Door',
            opening_text='The clock mechanism seems to have revealed a hidden door.\n'
                         'Perhaps it will lead to something of worth.',
            choices=[
                choices.ChoiceInspectRoom('Open the Door', 'treasure_room', conditions=[conditions.OnlyOnce()]),
                choices.ChoiceNavigate('Leave room', level='level_2', room='grande_hall'),
            ],
        ),
        'treasure_room': interactions.thing.Thing(
            name='Treasure Room',
            opening_text='The door opens to reveal a treasure room. A large iron chest is chained to the floor.\n'
                         'A heavy lock seals the chest.\n'
                         'As you examine the lock the shadows around you form into a fiend made of black\n'
                         '"WHERE IS MY RING?!!" he shrieks loudly.',
            choices=[
                choices.ChoiceInspectRoom('Attack the Shadow', 'shadow_combat'),
                choices.ChoiceInspectRoom('Robert is that you?', 'robert',
                                          conditions=[conditions.OnlyOnce(), conditions.GameFlagTrue('robert')]),
            ],
        ),
        'shadow_combat': interactions.thing.Thing(
            name='Combat with Shadow',
            opening_text='The shadow wails an echoing shriek!',
            choices=[
                choices.ChoiceInspectRoom('Banish him with the cross!', 'banished',
                                          conditions=[conditions.PlayerHasItem(item.holy_cross)]),
                choices.ChoiceInspectRoom('Shoot Him!', 'shoot',
                                          conditions=[conditions.PlayerHasItem(item.crossbow)]),
                choices.ChoiceInspectRoom('Holy Water!', 'water',
                                          conditions=[conditions.PlayerHasItem(item.holy_water)]),
                choices.ChoiceInspectRoom('FIRE!', 'fire',
                                          conditions=[conditions.PlayerHasItem(item.flammable_oil)]),
                choices.ChoiceInspectRoom('Nitroglycerin!', 'nitro',
                                          conditions=[conditions.PlayerHasItem(item.nitro)]),
            ],
        ),
        'banished': interactions.thing.Thing(
            name='Combat with Shadow',
            opening_text='You hold the cross forward and recite prayer.\n'
                         'The cross glows ever brighter as the shadow shrieks and shrinks away\n'
                         'until there is nothing but beaming light. The Chest is yours for the taking.',
            choices=[
                choices.ChoiceInspectRoom('Open Chest', 'chest'),
            ],
        ),
        'shoot': interactions.thing.Thing(
            name='Combat with Shadow',
            opening_text='You aim quickly and shoot a bolt at the menacing shadow.\n'
                         'The bolt goes through him and gets lodged in the treasure chest.\n'
                         'The shadow then flies right through you!\n'
                         'A cold pain hits your lungs as you turn to face the shadow once more.',
            choices=[
                choices.ChoiceInspectRoom('Banish him with the cross!', 'banished',
                                          conditions=[conditions.PlayerHasItem(item.holy_cross)]),
                choices.ChoiceInspectRoom('Holy Water!', 'water', conditions=[conditions.RoomFlagFalse('water')]),
                choices.ChoiceInspectRoom('FIRE!', 'fire', conditions=[conditions.PlayerHasItem(item.flammable_oil)]),
                choices.ChoiceInspectRoom('Nitroglycerin!', 'nitro', conditions=[conditions.PlayerHasItem(item.nitro)]),
            ],
            events=[
                events.SetRoomFlagTrue('shoot')
            ]
        ),
        'water': interactions.thing.Thing(
            name='Combat with Shadow',
            opening_text='You splash the water at the shadow only for it to pass through him and spread on the floor.\n'
                         'The shadow flies through you leaving an echoing ring in your ears. You grow dizzy.',
            choices=[
                choices.ChoiceInspectRoom('Banish him with the cross!', 'banished',
                                          conditions=[conditions.PlayerHasItem(item.holy_cross)]),
                choices.ChoiceInspectRoom('Shoot Him!', 'shoot', conditions=[conditions.RoomFlagFalse('shoot')]),
                choices.ChoiceInspectRoom('FIRE!', 'fire', conditions=[conditions.PlayerHasItem(item.flammable_oil)]),
                choices.ChoiceInspectRoom('Nitroglycerin!', 'nitro', conditions=[conditions.PlayerHasItem(item.nitro)]),
            ],
            events=[
                events.SetRoomFlagTrue('water'),
                events.RemoveItem(item.holy_water),  # todo: @alon remove it after use right?
            ]
        ),
        'fire': interactions.thing.Thing(
            name='Combat with Shadow',
            opening_text='You quickly pour the oil in a wide arch between you and the shadow.\n'
                         'As the evil shade charges forward you ignite the oil with your flint.\n'
                         'The shadow shrieks and burns before you. When the flames dies the chest remains.',
            choices=[
                choices.ChoiceInspectRoom('Open Chest', 'chest'),
                events.RemoveItem(item.flammable_oil),  # todo: @alon remove it after use right?
            ],
        ),
        'nitro': interactions.thing.Thing(
            name='Combat with Shadow',
            opening_text='You jump back out of the room as you toss the vial of nitroglycerin inside.\n'
                         'A loud explosion sends debris and smoke flying out through the door.\n'
                         'As you look inside the shadow is gone, but the chest and its contents have been destroyed.',
            choices=[
                choices.ChoiceNavigate('Leave room', level='level_2', room='grande_hall'),
            ],
            events=[
                events.SetRoomFlagTrue('found_treasure'),
                events.RemoveItem(item.nitro),  # todo: @alon remove it after use right?
            ]
        ),
        'robert': interactions.thing.Thing(
            name='Robert',
            opening_text='Yes it is I! What of it?',
            choices=[
                choices.ChoiceInspectRoom('What do you know of mistress?', 'robert_mistress'),
                choices.ChoiceInspectRoom('Why are you guarding this chest?', 'robert_chest'),
                choices.ChoiceInspectRoom('Attack the Shadow', 'shadow_combat'),
            ],
        ),
        'robert_chest': interactions.thing.Thing(
            name='Robert',
            opening_text='My wedding ring is inside, it is the key to my salvation!\n'
                         'None can have it but me! I shall not let you take my ring!',
            choices=[
                choices.ChoiceInspectRoom('What do you know of mistress?', 'robert_mistress',
                                          conditions=[conditions.OnlyOnce()]),
                choices.ChoiceInspectRoom('You mean this ring? (Present the ring)', 'robert_ring',
                                          conditions=[conditions.PlayerHasItem(item.engagement_ring)]),
                choices.ChoiceInspectRoom('Attack the Shadow', 'shadow_combat'),
            ],
        ),
        'robert_mistress': interactions.thing.Thing(
            name='Robert',
            opening_text='She is a temptress! I used to own this estate, yet she has played me for a fool!\n'
                         'I loved her and vowed to marry her, but then i found out what she was...\n'
                         'i refused to marry her! Nay "IT"! So i was cursed into this abysmal state! I need my ring!',
            choices=[
                choices.ChoiceInspectRoom('Why are you guarding this chest?', 'robert_chest',
                                          conditions=[conditions.OnlyOnce()]),
                choices.ChoiceInspectRoom('You mean this ring? (Present the ring)', 'robert_ring',
                                          conditions=[conditions.PlayerHasItem(item.engagement_ring)]),
                choices.ChoiceInspectRoom('Attack the Shadow', 'shadow_combat'),
            ],
            events=[events.UnlockJournal(entry.robert_mistress)]
        ),
        'robert_ring': interactions.thing.Thing(
            name='Robert',
            opening_text='YES! YES! This is the one! I must have it! can i have it?!',
            choices=[
                choices.ChoiceInspectRoom('Can i have what is in the chest?', 'robert_ring2'),
                choices.ChoiceInspectRoom('No, Attack the Shadow!', 'shadow_combat'),
            ],
        ),
        'robert_ring2': interactions.thing.Thing(
            name='Robert',
            opening_text='She fooled me again! I thought the ring was in the chest!\n'
                         'Nevermind... Yes have the chest! Now give me the ring!',
            choices=[
                choices.ChoiceInspectRoom('Give Ring', 'gave_ring'),
                choices.ChoiceInspectRoom('Attack the Shadow!', 'shadow_combat'),
            ],
            events=[events.UnlockJournal(entry.robert_ring)]
        ),
        'gave_ring': interactions.thing.Thing(
            name='Robert',
            opening_text='The ring floats gently from your hand and robert swirls around it.\n'
                         'with a sharp glow he vanishes, leaving behind a few fading sparks.',
            choices=[
                choices.ChoiceInspectRoom('Open Chest', 'chest'),
            ],
            events=[
                events.RemoveItem(item.engagement_ring),
            ],
        ),
        'chest': interactions.thing.Thing(
            name='Chest',
            opening_text='You open the chest and find a stack of gold coins and a mummified head.\n'
                         'A note attached to the head reads "Robert".',
            # todo: @alon do we want to add the stack of coins as item?
            choices=[
                choices.ChoiceNavigate('Leave room', level='level_2', room='grande_hall'),
            ],
            events=[
                events.SetRoomFlagTrue('found_treasure'),
                events.UnlockJournal(entry.found_treasure),
                events.AddItem(item.head)
            ],
        ),
        # gargoyle fight
        'gargoyle_fight': interactions.thing.Thing(
            name='Dining Room',
            opening_text='You rush into the dining room, jump onto the marble table and continue to try\n'
                         'and put as much distance between you and the hulking beast.\n'
                         'You turn back just as the gargoyle enters the room and slams the table.\n'
                         'The blow sends you flying in the air like a catapult.\n'
                         'You fly over the gargoyles head and manage to land in a diving roll\n'
                         'and escape back to the Grande Hall.',
        )
    }
)

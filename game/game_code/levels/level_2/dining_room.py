from game_code import interactions
from game_code.interactions.lib import choices, events, conditions
from game_code.objects import item, entry


dining_room = interactions.room.Room(
    name='Dining Room',
    opening_text='You enter the dining room. A long marble table runs the length of the decorated chamber.\n'
                 'Carved wooden chairs surround the table on both sides.',
    room_flags={'found_treasure': False, 'door_open': False},
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
        'shadow_combat': interactions.combat.Combat(
            name='Combat with Shadow',
            # todo: @inbar complete the combat
            opening_text='Combat - work in progress - you win!',
            choices=[
                choices.ChoiceNavigate('Leave room (temp)', level='level_2', room='grande_hall'),  # temp
            ],
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
                choices.ChoiceInspectRoom('Give Ring', 'chest_friendly'),
                choices.ChoiceInspectRoom('Attack the Shadow!', 'shadow_combat'),
            ],
            events=[events.UnlockJournal(entry.robert_ring)]
        ),
        'chest_friendly': interactions.thing.Thing(
            name='Chest',
            opening_text='The ring floats gently from your hand and robert swirls around it.\n'
                         'with a sharp glow he vanishes, leaving behind a few fading sparks.\n'
                         'You open the chest and find a stack of gold coins and a mummified head.\n'
                         'A note attached to the head reads "Robert".',
            # todo: @alon do we want to add the stack of coins or Roberts head as items?
            choices=[
                choices.ChoiceNavigate('Leave room', level='level_2', room='grande_hall'),
            ],
            events=[
                events.RemoveItem(item.engagement_ring),
                events.SetRoomFlagTrue('found_treasure'),
                events.UnlockJournal(entry.found_treasure)
            ],
        ),
        # 'chest_victory': interactions.thing.Thing(
        #     name='Chest',
        #     opening_text='The ring floats gently from your hand and robert swirls around it.\n'
        #                  'with a sharp glow he vanishes, leaving behind a few fading sparks.\n'
        #                  'You open the chest and find a stack of gold coins and a mummified head.\n'
        #                  'A note attached to the head reads "Robert".',
        #     # todo: @alon do we want to add the stack of coins or Roberts head as items?
        #     choices=[
        #         choices.ChoiceNavigate('Leave room', level='level_2', room='grande_hall'),
        #     ],
        #     events=[
        #         events.SetRoomFlagTrue('found_treasure'),
        #         events.UnlockJournal(entry.found_treasure)
        #     ],
        # ),
    }
)
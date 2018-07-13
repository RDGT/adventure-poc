from game_code import interactions
from game_code.interactions.lib import choices, events, conditions
from game_code.objects import item, entry

kitchen = interactions.room.Room(
    name='Kitchen',
    opening_text='You walk into what used to be a marvelous kitchen.\n'
                 'Cobwebs and dust cover every part of the room.\n'
                 'On the floor before you lies a corpse, chained to the large stone stove.\n'
                 'The corpse is shriveled from decay and is... mumbling...',
    choices=[
        choices.ChoiceInspectRoom(
            text='Kneel next to the zombie and listen.',
            scene='listen_to_zombie_1',
            conditions=[conditions.OnlyOnce()]
        ),
        choices.ChoiceInspectRoom(
            text='Destroy this creature and relieve him from his torment.',
            scene='destroy_zombie',
            conditions=[conditions.OnlyOnce()]
        ),
        choices.ChoiceNavigate('Leave room', level='level_1', room='entrance_hall'),
    ],
    scenes={
        'destroy_zombie': interactions.thing.Thing(
            name='Destroy Zombie',
            opening_text='As you come closer to the zombie his mumbles become clearer:\n'
                         '"Mistress... Im sorry. I tried to run away... I shouldn\'t have tried to run away".\n'
                         'He has two bite marks on his neck.',
            choices=[
                choices.ChoiceInspectRoom(
                    'Search the ashes',
                    scene='ashes'
                ),
                choices.ChoiceNavigate('Leave room', level='level_1', room='entrance_hall'),
            ]
        ),
        'ashes': interactions.thing.Thing(
            name='Pile of Ashes',
            opening_text='You swipe the ashes with your boot and find what seems to be an engagement ring.\n'
                         'It looks very valuable.',
            choices=[choices.ChoiceNavigate('Leave room', level='level_1', room='entrance_hall')],
            events=[events.AddItem(item.engagement_ring), events.UnlockJournal(entry.acquired_ring)]
        ),
        'listen_to_zombie_1': interactions.thing.Thing(
            name='Listen To Zombie',
            opening_text='As you come closer to the zombie his mumbles become clearer:\n'
                         '"Mistress... Im sorry. I tried to run away... I shouldn\'t have tried to run away".\n'
                         'He has two bite marks on his neck.',
            choices=[
                choices.ChoiceInspectRoom(
                    text='Ask why he tried to run away',
                    scene='listen_to_zombie_2',
                ),
                choices.ChoiceInspectRoom(
                    text='Destroy zombie',
                    scene='destroy_zombie',
                ),
            ],
            events=[events.UnlockJournal(entry.kitchen_zombie_mistress)]
        ),
        'listen_to_zombie_2': interactions.thing.Thing(
            name='Listen To Zombie',
            opening_text='The mistress is looking for a groom. She must not find one.\n'
                         'I have the ring. She must not get the ring.',
            choices=[
                choices.ChoiceInspectRoom(
                    text='Ask for the ring',
                    scene='listen_to_zombie_2',
                ),
                choices.ChoiceInspectRoom(
                    text='Put him out of his misery',
                    scene='destroy_zombie',
                ),
            ],
        ),
        'listen_to_zombie_3': interactions.thing.Thing(
            name='Listen To Zombie',
            opening_text='The zombie slowly reaches for his own abdomen and forces his hand inside,\n'
                         'pushing through the soft and rotten flesh.\n'
                         'He then pulls it out and hands you an adorned wedding ring.',
            choices=[choices.ChoiceNavigate('Leave room', level='level_1', room='entrance_hall')],
            events=[events.AddItem(item.engagement_ring), events.UnlockJournal(entry.acquired_ring)],
        ),
    }
)

from game.code import interactions
from game.code.interactions.lib import choices, events, conditions, scene
from game.code.objects import item, entry

bedroom = interactions.room.Room(
    name='Bedroom',
    opening_text='You enter a lavish bedroom, but instead of a bed there is a large and beautiful coffin.\n'
                 'A vampire must certainly live here, the velvet lining on the coffin makes you certain.\n'
                 'A towering mirror is attached to the wall.',
    choices=[
        choices.ChoiceInspectRoom(text='Examine the mirror', scene='mirror'),
        choices.ChoiceNavigate('Leave room', level='level_2', room='grande_hall'),
    ],
    screens={
        'revealed': scene.Screen(
            title='Bedroom',
            text='You enter a lavish bedroom, but instead of a bed there is a large and beautiful coffin.\n'
                 'A vampire must certainly live here, the velvet lining on the coffin makes you certain.\n'
                 'A stone passage leads to a Statue Room where a mirror used to be',
            choices=[
                choices.ChoiceNavigate('Enter the Statue room', level='level_2', room='statue_room'),
                choices.ChoiceNavigate('Leave room', level='level_2', room='grande_hall'),
            ]
        )
    },
    scenes={
        'mirror': interactions.thing.Thing(
            name='Mirror',
            opening_text='You come closer to te mirror. A number of demonic faces decorate the frame.\n'
                         'All of them are holding different gems in their mouths. One of them is missing a gem.',
            choices=[
                choices.ChoiceInspectRoom(text='Tap the mirror', scene='tap'),
                choices.ChoiceInspectRoom(text='place gem in the open socket', scene='gem',
                                          conditions=[conditions.PlayerHasItem(item.gem)]),
                choices.ChoiceNavigate('Leave room', level='level_2', room='grande_hall'),
            ],
        ),
        'gem': interactions.thing.Thing(
            name='Mirror Passage',
            opening_text='The gem fits perfectly into the socket.\n'
                         'A rumbling of heavy cogs shifts the mirror to the side to reveal a large stone passage.\n'
                         'A dimly lit room filled with statues is ahead.',
            choices=[
                choices.ChoiceNavigate('Enter the Statue room', level='level_2', room='statue_room'),
                choices.ChoiceNavigate('Leave room', level='level_2', room='grande_hall'),
            ],
            events=[
                events.SetRoomScreen('revealed'),
            ]
        ),
        'tap': interactions.thing.Thing(
            name='Mirror Passage',
            opening_text='Tapping on the mirror you can hear a hollow sound.\n'
                         'There is a passage behind the mirror but it seems too large to move by hand.',
            choices=[
                choices.ChoiceInspectRoom('Break the mirror', scene='break'),
                choices.ChoiceInspectRoom(text='place gem in the open socket', scene='gem',
                                          conditions=[conditions.PlayerHasItem(item.gem)]),
                choices.ChoiceNavigate('Leave room', level='level_2', room='grande_hall'),
            ],
        ),
        'break': interactions.thing.Thing(
            name='Mirror Passage',
            opening_text='You kick the mirror with all your strength!\n'
                         'Large shards of glass fly into the the dark room beyond\n'
                         'as the remaining pieces fall to the floor and shatter loudly.\n'
                         'A roar is heard from the darkness as a hulking stone gargoyle barrels towards you!',
            choices=[
                choices.ChoiceNavigate('Fight the Gargoyle!', level='level_2', room='statue_room', scene='fight1'),
            ],
            events=[
                events.SetRoomScreen('revealed'),
            ]
        ),
    }
)

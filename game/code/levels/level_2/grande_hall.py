from code import interactions
from code.interactions.lib import choices, events, conditions, scene
from code.objects import item, entry

grande_hall = interactions.room.Room(
    name='Grande Hall',
    opening_text='You descend down the stairs into a grande hall. Before you stands a well dressed ghoul.\n'
                 'He is busy sweeping the floor when he lifts his gaze and notices you.\n'
                 'His croaking voice mutters: "ah, a visitor."',
    choices=[
        choices.ChoiceInspectRoom('Speak with the Ghoul', 'speak'),
        choices.ChoiceInspectRoom('Attack Ghoul', 'attack'),
    ],
    room_flags={'clock_changed': False},
    screens={
        'grande_hall': scene.Screen(
            title='Grande Hall',
            text='Four doors lead away from the chamber, there is an old wooden clock standing on the left.',
            choices=[
                choices.ChoiceNavigate('Dining Room', level='level_2', room='dining_room'),
                choices.ChoiceNavigate('Library', level='level_2', room='library'),
                choices.ChoiceNavigate('Laboratory', level='level_2', room='laboratory'),
                choices.ChoiceNavigate('Bedroom', level='level_2', room='bedroom'),
                choices.ChoiceInspectRoom('Wooden Clock', 'clock',
                                          conditions=[conditions.RoomFlagFalse('clock_changed')]),
                choices.ChoiceInspectRoom('Wooden Clock', 'clock_changed',
                                          conditions=[conditions.RoomFlagTrue('clock_changed')]),
                choices.ChoiceNavigate('Go back to the living room', level='level_1', room='living_room'),
            ]
        ),
    },
    scenes={
        # ghoul scenes
        'attack': interactions.thing.Thing(
            name='Combat with Ghoul',
            opening_text='Choose your weapon',
            choices=[
                choices.ChoiceInspectRoom('Holy Cross', 'cross',
                                          conditions=[conditions.PlayerHasItem(item.holy_cross)]),
                choices.ChoiceInspectRoom('Crossbow', 'crossbow',
                                          conditions=[conditions.PlayerHasItem(item.crossbow)]),
                choices.ChoiceInspectRoom('Holy water', 'water',
                                          conditions=[conditions.PlayerHasItem(item.holy_water)]),
                choices.ChoiceInspectRoom('burn with oil', 'burn',
                                          conditions=[conditions.PlayerHasItem(item.flammable_oil)]),
            ],
        ),
        'cross': interactions.thing.Thing(
            name='Combat with Ghoul',
            opening_text='You raise you cross before the ghoul.\n'
                         'He hisses and cowers away from the light.\n'
                         'You advance towards him as his skin melts away,\n'
                         'then this flesh until he crumbles into a pile of bones.',
            events=[events.SetRoomScreen('grande_hall'), events.UnlockJournal(entry.ghoul_defeated)],
            choices=[choices.ChoiceBackToRoom('Observe the Grande Hall')],
        ),
        'crossbow': interactions.thing.Thing(
            name='Combat with Ghoul',
            opening_text='Without hesitation you raise your crossbow and shoot a bolt straight into the gouls heart.\n'
                         'The power of the blow sends him flying to his back where he lies motionless.',
            events=[events.SetRoomScreen('grande_hall'), events.UnlockJournal(entry.ghoul_defeated)],
            choices=[choices.ChoiceBackToRoom('Observe the Grande Hall')],
        ),
        'water': interactions.thing.Thing(
            name='Combat with Ghoul',
            opening_text='With a sudden swift motion you splash the butler with the holy water.\n'
                         'He barely has time to scream before he melts down to the floor in a puddle of ooz.',
            events=[
                events.SetRoomScreen('grande_hall'),
                events.UnlockJournal(entry.ghoul_defeated),
                events.RemoveItem(item.holy_water),  # todo: @alon remove it after use right?
            ],
            choices=[choices.ChoiceBackToRoom('Observe the Grande Hall')],
        ),
        'burn': interactions.thing.Thing(
            name='Combat with Ghoul',
            opening_text='You bite the cork off from the oil bottle and splash the contents on the ghoul.\n'
                         'At first he is simply surprised but his look turns into fear\n'
                         'as the sparks from your flint fly in his direction.\n'
                         'The oil catches flames and the ghoul screams.\n'
                         'Within a few moments there is nothing but ashe.',
            events=[
                events.SetRoomScreen('grande_hall'),
                events.UnlockJournal(entry.ghoul_defeated),
                events.RemoveItem(item.flammable_oil),  # todo: @alon remove it after use right?
            ],
            choices=[choices.ChoiceBackToRoom('Observe the Grande Hall')],
        ),
        'speak': interactions.thing.Thing(
            name='Ghoul',
            opening_text='You bow gracefully before the ghoul and he bows back.\n'
                         'The ghoul speaks again: "good evening sir. How may i be of service?"',
            prompt='what do you say?',
            choices=[
                choices.ChoiceInspectRoom('I am looking for the mistress. Is she present?', 'speak_mistress1'),
                choices.ChoiceInspectRoom(
                    'Good evening to you as well. Are there other servants in this place?', 'speak_robert'),
            ],
        ),
        'speak_robert': interactions.thing.Thing(
            name='Ghoul',
            opening_text='Other servants? Well lets see...I guess the only "servant"\n'
                         'other than me would be Robert, but he is currently... Indisposed.\n'
                         'He has been searching for that ring of his for what seems like.. an eternity.',
            choices=[
                choices.ChoiceInspectRoom('Ask to meet mistress', 'speak_mistress2'),
                choices.ChoiceInspectRoom('Attack Ghoul', 'attack'),
            ],
            events=[
                events.UnlockJournal(entry=entry.ask_about_servants_with_ring,
                                     conditions=[conditions.PlayerHasItem(item.engagement_ring)]),
                events.UnlockJournal(entry=entry.ask_about_servants_no_ring,
                                     conditions=[conditions.PlayerMissingItem(item.engagement_ring)]),
            ]
        ),
        'speak_mistress1': interactions.thing.Thing(
            name='Ghoul',
            opening_text='Ah yes. My mistress is in her chambers below. What would be your business with her?',
            prompt='what do you say?',
            choices=[
                choices.ChoiceInspectRoom('I only wish to meet her', 'speak_mistress2'),
            ],
            events=[events.UnlockJournal(entry.ghoul_mistress)]
        ),
        'speak_mistress2': interactions.thing.Thing(
            name='Ghoul',
            opening_text='"Ah, If you are to meet mistress you must be presentable."\n'
                         'The ghoul exposes his rotten fangs. "And by that i mean dead!".',
            choices=[
                choices.ChoiceInspectRoom('Attack Ghoul', 'attack'),
            ],
        ),
        # clock scenes
        'clock': interactions.thing.Thing(
            name='Old Clock',
            opening_text='The old oak wood clock is covered with dust.\n'
                         'Its mechanism seems to have gone silent many years ago.',
            choices=[
                choices.ChoiceInspectRoom('Move clock hand to 3:15', 'clock_changed',
                                          conditions=[
                                              conditions.GameFlagTrue('clock_scribble'),
                                              conditions.OnlyOnce(),
                                          ]),
                choices.ChoiceBackToRoom('Leave the clock'),
            ],
            events=[events.UnlockJournal(entry.examine_clock)]
        ),
        'clock_changed': interactions.thing.Thing(
            name='Old Clock',
            opening_text='As the mechanism clicks into place,\n'
                         'you hear a rumbling of stone echoing from the dining room.',
            future_text='The Clock shows 3:15, the mechanism in place',
            choices=[choices.ChoiceBackToRoom('Leave clock')],
            events=[
                events.SetRoomFlagTrue('clock_changed'),
                events.SetRoomFlagTrue('door_open', room='dining_room'),
                events.UnlockJournal(entry.clock_hands)
            ]
        ),
        # gargoyle fight
        'gargoyle_fight': interactions.thing.Thing(
            name='Grande Hall',
            opening_text='You flee from the beast into the Grande Hall.\n'
                         'The gargoyle gives chase, smashing his way through every passage to small to fit his size.',
            choices=[
                choices.ChoiceNavigate('Run to the Library',
                                       level='level_2', room='library', scene='gargoyle_fight',
                                       conditions=[conditions.OnlyOnce()]),
                choices.ChoiceNavigate('Run to the Laboratory',
                                       level='level_2', room='laboratory', scene='gargoyle_fight',
                                       conditions=[conditions.OnlyOnce()]),
                choices.ChoiceNavigate('Run to the Dining Room',
                                       level='level_2', room='dining_room', scene='gargoyle_fight',
                                       conditions=[conditions.OnlyOnce()]),
            ],
            events=[events.SetRoomFlagTrue('retreated', room='statue_room')]
        )
    }
)

from game_code import interactions
from game_code.interactions.lib import choices, events, conditions, scene
from game_code.objects import item, entry

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
        )
    },
    scenes={
        # ghoul scenes
        'attack': interactions.combat.Combat(
            name='Combat with Ghoul',
            # todo: @inbar complete the combat
            opening_text='Combat - work in progress - you win!',
            choices=[
                choices.ChoiceNavigate('Leave room (temp)', level='level_2', room='grande_hall'),  # temp
            ],
            events=[events.SetRoomScreen('grande_hall'), events.UnlockJournal(entry.ghoul_defeated)]
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
            events=[events.ConditionalUnlockJournal(
                [
                    (conditions.PlayerHasItem(item.engagement_ring), entry.ask_about_servants_with_ring),
                    (conditions.PlayerMissingItem(item.engagement_ring), entry.ask_about_servants_no_ring),
                ]
            )]
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
                choices.ChoiceNavigate('Leave the Clock', level='level_2', room='grande_hall'),
            ],
            events=[events.UnlockJournal(entry.examine_clock)]
        ),
        'clock_changed': interactions.thing.Thing(
            name='Old Clock',
            opening_text='As the mechanism clicks into place,\n'
                         'you hear a rumbling of stone echoing from the dining room.',
            future_text='The Clock shows 3:15, the mechanism in place',
            events=[
                events.SetRoomFlagTrue('clock_changed'),
                events.SetRoomFlagTrue('door_open', room='dining_room'),
                events.UnlockJournal(entry.clock_hands)
            ]
        ),
    }
)

from game_code import interactions
from game_code.interactions.lib import choices, events, conditions, scene
from game_code.objects import item, entry

laboratory = interactions.room.Room(
    name='Laboratory',
    opening_text='As you enter the room it seems different. This room has seen recent use.\n'
                 'A number of pipes and cauldrons are placed on burning coals.\n'
                 'A chemistry apparatus next to the door is boiling strange fluids. This is a laboratory.',
    room_flags={'lock_box_broken': False, 'made_nitro': False},
    choices=[
        choices.ChoiceInspectRoom(text='Chemistry Apparatus', scene='apparatus',
                                  conditions=[conditions.RoomFlagFalse('made_nitro')]),
        choices.ChoiceInspectRoom(text='Little Lock Box', scene='lock_box',
                                  conditions=[conditions.RoomFlagFalse('lock_box_broken')]),
        choices.ChoiceNavigate('Leave room', level='level_1', room='entrance_hall'),
    ],
    scenes={
        'apparatus': interactions.thing.Thing(
            name='Chemistry Apparatus',
            opening_text='On the main stone table there is an elaborate chemistry apparatus.\n'
                         'Various glass pipes dripping along and mixing slowly.',
            choices=[
                choices.ChoiceInspectRoom(text='Make Nitroglycerin', scene='nitro'),
                choices.ChoiceInspectRoom(text='Little Lock Box', scene='lock_box',
                                          conditions=[conditions.RoomFlagFalse('lock_box_broken')]),
                choices.ChoiceNavigate('Leave room', level='level_1', room='entrance_hall'),
            ],
        ),
        'nitro': interactions.thing.Thing(
            name='Chemistry Apparatus',
            opening_text='You turn a couple of valves and the fluids flow faster, filling up the end vial.\n'
                         'You recognise the smell. This is nitroglycerin. You pocket the vial.',
            choices=[
                choices.ChoiceInspectRoom(text='Little Lock Box', scene='lock_box',
                                          conditions=[conditions.RoomFlagFalse('lock_box_broken')]),
                choices.ChoiceNavigate('Leave room', level='level_1', room='entrance_hall'),
            ],
            events=[
                events.UnlockJournal(entry.make_nitro),
                events.AddItem(item.nitro),
                events.SetRoomFlagTrue('made_nitro'),
            ]
        ),
        'lock_box': interactions.thing.Thing(
            name='Small Lock Box',
            opening_text='You notice a small lock box sitting on a table. You rattle it and hear something inside.\n'
                         'You smash the box open using the stock of your crossbow.\n'
                         'Inside is a beautifully cut ruby the size of your fist.',
            choices=[
                choices.ChoiceInspectRoom(text='Chemistry Apparatus', scene='apparatus',
                                          conditions=[conditions.RoomFlagFalse('made_nitro')]),
                choices.ChoiceNavigate('Leave room', level='level_1', room='entrance_hall'),
            ],
            events=[
                events.UnlockJournal(entry.little_lock_box),
                events.SetRoomFlagTrue('lock_box_broken'),
            ]
        ),
    }
)

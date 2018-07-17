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
        choices.ChoiceNavigate('Leave room', level='level_2', room='grande_hall'),
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
                choices.ChoiceNavigate('Leave room', level='level_2', room='grande_hall'),
            ],
        ),
        'nitro': interactions.thing.Thing(
            name='Chemistry Apparatus',
            opening_text='You turn a couple of valves and the fluids flow faster, filling up the end vial.\n'
                         'You recognise the smell. This is nitroglycerin. You pocket the vial.',
            choices=[
                choices.ChoiceInspectRoom(text='Little Lock Box', scene='lock_box',
                                          conditions=[conditions.RoomFlagFalse('lock_box_broken')]),
                choices.ChoiceNavigate('Leave room', level='level_2', room='grande_hall'),
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
                choices.ChoiceNavigate('Leave room', level='level_2', room='grande_hall'),
            ],
            events=[
                events.UnlockJournal(entry.little_lock_box),
                events.AddItem(item.gem),
                events.SetRoomFlagTrue('lock_box_broken'),
            ]
        ),
        # gargoyle fight
        'gargoyle_fight': interactions.thing.Thing(
            name='Laboratory',
            opening_text='Running into the laboratory you narrowly avoid another stone fist.\n'
                         'The gargoyle looses ballance and crashes into a cauldron,\n'
                         'sending sparks of fire in every direction.\n'
                         'The gargoyle, covered in flames rears for another attack.',
            choices=[choices.ChoiceInspectRoom('Bait the gargoyle', 'gargoyle_bait')]
        ),
        'gargoyle_bait': interactions.thing.Thing(
            name='Laboratory',
            opening_text='You position yourself behind the chemistry apparatus.\n'
                         'The gargoyle shakes the room with a mighty roar and charges straight at you.\n'
                         'Just at the right time you leap out of the way as the gargoyle\n'
                         'collides with the nitro filled glass.\n'
                         'A large explosion catches you mid air and slams you against the wall.',
            choices=[choices.ChoiceInspectRoom('Stand up', 'gargoyle_gone')]
        ),
        'gargoyle_gone': interactions.thing.Thing(
            name='Laboratory',
            opening_text='Standing back up you prepare for another attack but as the smoke settles\n'
                         'the only thing left of the gargoyle are nothing more than scattered rocks.\n'
                         'The path in the statue room is now clear.',
            choices=[
                choices.ChoiceNavigate('Go back to the Grande Hall', level='level_2', room='grande_hall'),
                choices.ChoiceNavigate('Go back to the Statue Room', level='level_2', room='statue_room'),
            ],
            events=[events.SetRoomScreen('clear', room='statue_room')]
        )
    }
)

from game.code import interactions
from game.code.interactions import choices, events, conditions
from game.code.objects import item, entry


living_room = interactions.room.Room(
    name='Living Room',
    opening_text='The old wooden door is barely hanging by one bent hinge,\n'
                 'you push it ever so slightly and it falls flat on the chamber floor producing a loud thud\n'
                 'and sending a cloud of dust that fills the air. As soon as you take one step,\n'
                 'the dust fog forms into a ghastly image\n'
                 'releasing a foul scream and charging at you with horrid intent!',
    future_text='The old wooden door is barely hanging by one bent hinge',
    room_flags={'ghast_dead': False},
    choices=[
        choices.ChoiceInspectRoom(
            text='Hold your holy cross firmly before the ghost and recite a banishment prayer!',
            scene='ghast_destroyed',
            conditions=[conditions.OnlyOnce(), conditions.RoomFlagFalse('ghast_dead'),
                        conditions.PlayerHasItem(item.holy_cross)],
        ),
        choices.ChoiceInspectRoom(
            text='Stand your ground. There is nothing to fear. God is on your side.',
            scene='ghast_illusion',
            conditions=[conditions.OnlyOnce(), conditions.RoomFlagFalse('ghast_dead')],
        ),
        choices.ChoiceInspectRoom(
            text='Go to the Iron Gate',
            scene='iron_gate',
            conditions=[conditions.RoomFlagTrue('ghast_dead')]
        ),
    ],
    scenes={
        'ghast_destroyed': interactions.thing.Thing(
            name='Ghast Destroyed',
            opening_text='s soon as you raise the cross the ghast darts away from its light.\n'
                         'You continue reciting prayer as you advance at the ever shrinking cloud of evil.\n'
                         'As you finish the prayer the cross lets out a blinding light,\n'
                         'the ghast shrieks and vanishes into thin air.',
            choices=[
                choices.ChoiceInspectRoom(
                    text='Move towards the iron gate at the far end of the room',
                    scene='iron_gate'
                ),
                choices.ChoiceNavigate('Go back to Entrance Hall', level='level_1', room='entrance_hall'),
            ],
            events=[events.UnlockJournal(entry.destroy_ghast), events.SetRoomFlagTrue('ghast_dead')]
        ),
        'ghast_illusion': interactions.thing.Thing(
            name='Ghast Illusion',
            opening_text='The ghast charges at you yet you stand firmly, staring into its glowing eyes.\n'
                         'As it reaches you it disperses into thin air. Nothing but an illusion.',
            choices=[
                choices.ChoiceInspectRoom(
                    text='Move towards the iron gate at the far end of the room',
                    scene='iron_gate'
                ),
                choices.ChoiceNavigate('Go back to Entrance Hall', level='level_1', room='entrance_hall'),
            ],
            events=[events.UnlockJournal(entry.stand_ground), events.SetRoomFlagTrue('ghast_dead')]
        ),
        'iron_gate': interactions.thing.Thing(
            name='Iron Gate',
            opening_text='The iron gate is locked. Behind it is a flight of stairs leading down',
            choices=[
                choices.ChoiceInspectRoom(
                    text='Try the key',
                    scene='gate_unlocked',
                    conditions=[conditions.PlayerHasItem(item.iron_key)]
                ),
                choices.ChoiceNavigate('Go back to Entrance Hall', level='level_1', room='entrance_hall'),
            ],
        ),
        'gate_unlocked': interactions.thing.Thing(
            name='Iron Gate',
            opening_text='The key unlocked the gate and it swings open,\n'
                         'the sound of its rusty hinges echos down the stairs.',
            choices=[
                choices.ChoiceNavigate(
                    text='Advance down the stairs',
                    level='level_2', room='grande_hall'
                ),
                choices.ChoiceNavigate('Go back to Entrance Hall', level='level_1', room='entrance_hall'),
            ],
            events=[events.UnlockJournal(entry.use_key)]
        ),
    }
)

from game_code import interactions


iron_gate2 = interactions.scene.Scene(
    name='Iron Gate',
    opening_text='The key fits and the gate swings open, the sound of its rusty hinges echos down the stairs',
    options={
        'Advance down the stairs': 'level_2.grande_hall.grande_hall1',
        'Go back to the entrance hall': 'level_1.entrance_hall.entrance_hall',
    }
)

iron_gate1 = interactions.scene.Scene(
    name='Iron Gate',
    opening_text='The iron gate is locked. Behind it is a flight of stairs leading down.',
    options={
        'Try the key': 'level_1.living_room.iron_gate2',
        'Go back to the entrance hall': 'level_1.entrance_hall.entrance_hall',
    }
)


hold_cross = interactions.scene.Scene(
    name='Conflict with a Ghast',
    opening_text='As soon as you raise the cross the ghast darts away from its light.\n'
                 'You continue reciting prayer as you advance at the ever shrinking cloud of evil.\n'
                 'As you finish the prayer the cross lets out a blinding light,\n'
                 'the ghast shrieks and vanishes into thin air.',
    # todo: combat
    options={
        'Move towards the iron gate at the far end of the room.': 'level_1.living_room.iron_gate1',
        'Go back to the entrance hall': 'level_1.entrance_hall.entrance_hall',
    }
)

stand_ground = interactions.scene.Scene(
    # todo: alon to complete
    name='Conflict with a Ghast',
    opening_text='ghast dissipates',
    options={
        'Go back to the entrance hall': 'level_1.living_room.iron_gate1',
    }
)


living_room = interactions.room.Room(
    name='Living Room',
    opening_text='The old wooden door is barely hanging by one bent hinge,\n'
                 'you push it ever so slightly and it falls flat on the chamber floor producing a loud **thud**\n'
                 'and sending a cloud of dust that fills the air. As soon as you take one step,\n'
                 'the dust fog forms into a ghastly image\n'
                 'releasing a foul scream and charging at you with horrid intent!',
    options={
        'Hold your holy cross firmly before the ghost and recite a banishment prayer!':
            'level_1.living_room.hold_cross',
        'Stand your ground. There is nothing to fear. God is on your side':
            'level_1.living_room.stand_ground',
    }
)

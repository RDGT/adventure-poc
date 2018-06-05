from game_code import interactions


listen_to_zombie = interactions.scene.Scene(
    # todo: alon to complete
    name='Kitchen',
    opening_text='silence',
    options={
        'Leave room': 'level_1.entrance_hall.entrance_hall',
    }
)

zombie_ashes = interactions.scene.Scene(
    name='Zombie Ashes',
    opening_text='You swipe the ashes with your boot and find what seems to be an engagement ring.\n'
                 'It looks very valuable',
    options={
        'Leave room': 'level_1.entrance_hall.entrance_hall',
    }
)

kill_zombie = interactions.scene.Scene(
    name='Kitchen Floor',
    opening_text='The zombie collapses into ashe',
    options={
        'Search the ashes': 'level_1.kitchen.zombie_ashes',
        'Leave room': 'level_1.entrance_hall.entrance_hall',
    }
)

kitchen = interactions.room.Room(
    name='Kitchen',
    opening_text='You walk into what used to be a marvelous kitchen.\n'
                 'Cobwebs and dust cover every part of the room.\n'
                 'On the floor before you lies a corpse, chained to the large stone stove.\n'
                 'The corpse is shriveled from decay and is... mumbling...',
    options={
        'Kneel next to the zombie and listen.': 'level_1.kitchen.listen_to_zombie',
        'Destroy this creature and relieve him from his torment.': 'level_1.kitchen.kill_zombie',
    }
)

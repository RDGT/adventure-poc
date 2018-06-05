from game_code import interactions

closet = interactions.scene.Scene(
    name='Closet',
    opening_text='As you open the closet a cloud of moths fly out,\n'
                 'a few stinking leather coats hang on frail hooks.\n'
                 'You search the pockets and eventually find a key',
    options={
        'Go back to the entrance hall': 'level_1.entrance_hall.entrance_hall',
    }
)

closet_room = interactions.room.Room(
    name='Closet Room',
    opening_text='The smell of wet leather fills the air.\n'
                 'Before you are a few vacant coat hangers and a rotting wooden closet.',
    options={
        'Search the closet': closet,
        'Leave room': 'level_1.entrance_hall.entrance_hall',
    }
)

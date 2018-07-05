from game_code import interactions
from game_code.interactions.lib import choices, events
from game_code.objects import item

closet_room = interactions.room.Room(
    name='Closet Room',
    opening_text='The smell of wet leather fills the air.\n'
                 'Before you are a few vacant coat hangers and a rotting wooden closet.',
    choices=[
        choices.ChoiceInspectRoom('Search the closet', 'closet', conditions=[choices.OnlyOnce()]),
        choices.ChoiceNavigate('Leave room', level='level_1', room='entrance_hall'),
    ],
    scenes={
        'closet': interactions.thing.Thing(
            name='Closet',
            opening_text='As you open the closet a cloud of moths fly out,\n'
                         'a few stinking leather coats hang on frail hooks.\n'
                         'You search the pockets and eventually find a key',
            events=[events.AddItem(item.Item('key', 'key from leather coat'))]
        )
    }
)

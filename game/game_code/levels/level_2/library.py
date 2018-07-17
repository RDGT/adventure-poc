from game_code import interactions
from game_code.interactions.lib import choices, events, conditions, scene
from game_code.objects import item, entry

library = interactions.room.Room(
    name='Library',
    opening_text='You enter a vast library.\n'
                 'a dozen rows of bookshelves bend under the weight of hundreds of old tomes.\n'
                 'A writing desk is pressed against the wall on the far end of the room.',
    choices=[
        choices.ChoiceInspectRoom(text='Search the writing desk', scene='desk', conditions=[conditions.OnlyOnce()]),
        choices.ChoiceNavigate('Leave room', level='level_1', room='entrance_hall'),
    ],
    scenes={
        'desk': interactions.thing.Thing(
            name='Writing Desk',
            opening_text='A few ink pads, vials and a feather.\n'
                         'A few empty scrolls and... a scribble of a clock. The hands point at 3:15. ',
            choices=[
                choices.ChoiceNavigate('Leave room', level='level_1', room='entrance_hall'),
            ],
            events=[
                events.UnlockJournal(entry.clock_scribble),
                events.SetGameFlagTrue('clock_scribble'),
            ]
        ),
    }
)

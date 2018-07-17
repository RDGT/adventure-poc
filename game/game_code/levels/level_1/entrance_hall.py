from game_code import interactions
from game_code.interactions.lib import choices, events
from game_code.objects import entry

entrance_hall = interactions.room.Room(
    name='Entrance Hall',
    opening_text='beyond the door is a circular wide room.\n'
                 'The air is moldy and the floor is covered with dust.\n'
                 'There are three doors leading away from the hall.',
    choices=[
        choices.ChoiceNavigate('Left door', level='level_1', room='closet_room'),
        choices.ChoiceNavigate('Front door', level='level_1', room='living_room'),
        choices.ChoiceNavigate('Right door', level='level_1', room='kitchen'),
    ],
    events=[events.UnlockJournal(entry.cursed_dungeon)],
)

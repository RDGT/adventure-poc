from game_code import interactions

test_room = interactions.room.Room(
    name='test room',
    opening_text='this room is just a test',
    prompt='what even can you do?',
)

puzzle = interactions.puzzle.MultipleChoice(
    name='hardest puzzle in the world',
    opening_text='what is 1+1?',
    prompt='do some math',
    correct_answer='Two',
    wrong_answers=['One', 'Three', 'Four'],
    success=interactions.the_end_win,
    failure=interactions.the_end_lose,
)


test_room.set_option('puzzle', puzzle)

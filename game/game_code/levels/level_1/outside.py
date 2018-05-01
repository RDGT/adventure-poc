from game_code import interactions
import entrance_hall

# 1. Kicking down the door,
# 2. Opening the door slowly,
# 3. Knocking and waiting for an answer.

outside = interactions.room.Room(
    name='Outside',
    opening_text='',
    prompt='what even can you do?',
    options={
        'kick': entrance_hall.entrance_hall_room,
        'open': entrance_hall.entrance_hall_room,
        'knock': entrance_hall.entrance_hall_room
    }
)
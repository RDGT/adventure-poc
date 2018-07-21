from lib import area


class Level(area.Area):

    def __init__(self, name, rooms=None):
        self.name = name
        if isinstance(rooms, list):
            rooms = {r: None for r in rooms}
        elif rooms is None:
            rooms = {}
        else:
            rooms = rooms
        self.rooms = rooms
        super(Level, self).__init__()

    def attach_game(self, game):
        for room in self.rooms.values():
            if room is not None:
                room.attach_game(game)
        super(Level, self).attach_game(game)

    def add_room(self, room_key, room_instance):
        """should add the room_instance to the self.rooms dict using room_key"""
        room_instance.attach_game(self.game)
        self.rooms[room_key] = room_instance

    def __getattr__(self, item):
        """convenience for loading rooms from the level"""
        if item in self.rooms:
            return self.rooms[item]
        super(Level, self).__getattr__(item)

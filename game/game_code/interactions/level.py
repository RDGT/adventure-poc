from lib import area


class Level(area.Area):

    def __init__(self):
        self.rooms = {}
        super(Level, self).__init__()

    def get_first_scene(self):
        raise NotImplementedError()

    def load_room(self, room_key, room_instance):
        """should add the room_instance to the self.rooms dict using room_key"""
        raise NotImplementedError()

    def load_rooms(self):
        """should load all rooms in this level and attach game"""
        raise NotImplementedError()

    def __getattr__(self, item):
        """convenience for loading rooms from the level"""
        if item in self.rooms:
            return self.rooms[item]
        super(Level, self).__getattr__(item)


class BasicLevel(Level):

    def load_room(self, room_key, room_instance):
        room_instance.attach_game(self.game)
        self.rooms[room_key] = room_instance


class Entity(object):
    def __init__(self):
        self.game = None
        super(Entity, self).__init__()

    def attach_game(self, game):
        self.game = game


class MenuItem(Entity):

    def __init__(self, name, description, **kwargs):
        self.name = name
        self.description = description
        self.kwargs = kwargs
        super(MenuItem, self).__init__()

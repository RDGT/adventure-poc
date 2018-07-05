from lib import entity


class Item(entity.Entity):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        super(Item, self).__init__()

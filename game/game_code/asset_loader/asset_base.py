from game_code import interactions
from game_code import objects
from collections import namedtuple


RoomAsset = namedtuple('RoomAsset', 'level_id room_object')
StoryStart = namedtuple('StoryStart', 'level_id room_id')


class AssetBase(object):

    def __init__(self):
        self.levels = {}
        self.rooms = {}
        self.items = {}
        self.entries = {}
        self.meta = {}
        self.story_start = None
        self.story_name = None
        self.starting_items = []
        self.starting_entries = []
        super(AssetBase, self).__init__()

    def generate_story(self):
        """combine all the rooms and levels together into a story"""

    def set_meta(self, meta_key, meta_value, **kwargs):
        self.meta[meta_key] = meta_value

    def set_story_starting_location(self, level_name, room_name):
        self.story_start = StoryStart(level_name, room_name)

    def set_story_name(self, story_name):
        self.story_name = story_name

    def add_level(self, level_id, name):
        if level_id not in self.levels:
            level = interactions.level.Level(name=name)
            self.levels[level_id] = level
        return self.levels[level_id]

    def add_room(self, level_id, room_id, name, opening_text, choices, **kwargs):
        room_object = interactions.room.Room(
            name=name,
            opening_text=opening_text,
            choices=choices,
            **kwargs
        )
        room_key = '{}.{}'.format(level_id, room_id)
        self.rooms[room_key] = RoomAsset(level_id, room_object)

    def add_item(self, item_id, item_name, item_description, **kwargs):
        self.items[item_id] = objects.item.Item(item_name, item_description, **kwargs)

    def add_entry(self, entry_id, entry_name, entry_description, **kwargs):
        self.entries[entry_id] = objects.item.Item(entry_name, entry_description, **kwargs)


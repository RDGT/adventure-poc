from game_code import interactions
from game_code import objects
from collections import namedtuple
import logging

log = logging.getLogger('asset_loader.base')

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

    def add_level(self, level_id, level_name):
        if level_id not in self.levels:
            level = interactions.level.Level(name=level_name)
            self.levels[level_id] = level
        return self.levels[level_id]

    def add_room(self, room_id, room_name, opening_text, choices, **kwargs):
        room_object = interactions.room.Room(
            name=room_name,
            opening_text=opening_text,
            choices=choices,
            **kwargs
        )
        self.rooms[room_id] = room_object

    def add_item(self, item_id, name, description, **kwargs):
        self.items[item_id] = objects.item.Item(name, description, **kwargs)

    def add_entry(self, entry_id, name, description, **kwargs):
        self.entries[entry_id] = objects.item.Item(name, description, **kwargs)

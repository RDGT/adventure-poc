import game_code.interactions as interactions
import game_code.core.exceptions as exceptions
import game_code.objects as objects
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

    def generate_story(self, game):
        """combine all the rooms and levels together into a story and give it to the game"""
        for level_id, level in self.levels.items():
            game.add_new_level(level_id, self._gen_level(level))
        game.set_opening_screen(self.story_start.level_id, self.story_start.room_id)

    def _gen_level(self, level):
        for room_id in level.rooms.keys():
            if room_id not in self.rooms:
                raise exceptions.AssetNotLoaded(room_id)
            level.add_room(room_id, self.rooms[room_id])

    def set_meta(self, meta_key, meta_value, **kwargs):
        self.meta[meta_key] = meta_value

    def set_story_starting_location(self, level_name, room_name):
        self.story_start = StoryStart(level_name, room_name)

    def set_story_name(self, story_name):
        self.story_name = story_name

    def add_level(self, level_id, level_name, rooms):
        level = interactions.level.Level(name=level_name, rooms=rooms)
        self.levels[level_id] = level

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

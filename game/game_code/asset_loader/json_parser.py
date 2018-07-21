import json
import os
from asset_base import AssetBase
from core import exceptions
import logging

log = logging.getLogger('asset_loader.json')


class JsonParser(AssetBase):
    """parses json files to populate the games levels, rooms, scenes, etc"""

    parse_func_frmt = '_parse_{}'

    def load_dir(self, directory_path):
        pass

    def load_file(self, file_path):
        with open(file_path, 'rb') as f:
            object_dict = json.load(f)
        try:
            self.parse_object_dict(object_dict)
        except Exception as exc:
            log.error('Exception parsing from file: file_path={} exc={}'.format(file_path, exc))
            raise

    def parse_object_dict(self, object_dict):
        object_type = object_dict.pop('type', None)
        if object_type is None:
            raise exceptions.NoTypeSpecified()
        parse_func = self._get_object_parser_func(object_type)
        parse_func(object_dict)

    def _get_object_parser_func(self, object_type):
        parse_func_name = self.parse_func_frmt.format(object_type)
        if not hasattr(self, parse_func_name):
            raise exceptions.NoSuchParser(object_type)
        parse_func = getattr(self, parse_func_name)
        return parse_func

    def _parse_level(self, level_dict):
        self.add_level(**level_dict)

    def _parse_room(self, room_dict):
        # todo: handle choices/screens/scenes and sub...
        self.add_room(**room_dict)

    def _parse_items(self, item_dict):
        for item_id, item in item_dict['items']:
            self.add_item(item_id, **item)

    def _parse_entries(self, entry_dict):
        for entry_id, entry in entry_dict['entries']:
            self.add_item(entry_id, **entry)

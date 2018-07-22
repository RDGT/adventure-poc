import json
import os
import asset_base
import game.code.core.exceptions as exceptions
import game.code.core
from game.code import interactions
import logging

log = logging.getLogger('asset_loader.json')


class JsonParser(asset_base.AssetBase):
    """parses json files to populate the games levels, rooms, scenes, etc"""

    parse_func_frmt = '_parse_{}'

    def load_story(self, story):
        story_dir = os.path.join(game.code.core.assets_dir, story)
        self.load_dir(story_dir)

    def load_dir(self, directory_path):
        for dirpath, dirnames, filenames in os.walk(directory_path):
            for file_name in [f for f in filenames if f.endswith(".json")]:
                file_path = os.path.join(dirpath, file_name)
                self.load_file(file_path)

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

    def _parse_config(self, config_dict):
        self.story_name = config_dict['story_name']
        self.set_story_starting_location(**config_dict['starting_location'])
        self.starting_items = config_dict.get('starting_items', [])
        self.starting_entries = config_dict.get('starting_entries', [])
    
    def _parse_items(self, item_dict):
        for item_id, item in item_dict['items'].items():
            self.add_item(item_id, **item)

    def _parse_entries(self, entry_dict):
        for entry_id, entry in entry_dict['entries'].items():
            self.add_item(entry_id, **entry)

    def _parse_level(self, level_dict):
        self.add_level(**level_dict)

    def _parse_room(self, room_dict):
        # todo: handle choices/screens/scenes and sub...
        choices = room_dict.pop('choices', [])
        room_dict['choices'] = self._sub_parse_choices(choices)
        events = room_dict.pop('events', [])
        room_dict['events'] = self._sub_parse_events(events)
        screens = room_dict.pop('screens', {})
        room_dict['screens'] = self._sub_parse_screens(screens)
        scenes = room_dict.pop('scenes', {})
        room_dict['scenes'] = self._sub_parse_scenes(scenes)
        self.add_room(**room_dict)
    
    def _sub_parse_choices(self, choice_list):
        return [self._sub_parse_choice(choice) for choice in choice_list]
    
    def _sub_parse_choice(self, choice_dict):
        choice_class = self.__load_class_from_module(interactions.choices, choice_dict.pop('type'))
        conditions = choice_dict.pop('conditions', [])
        choice_dict['conditions'] = self._sub_parse_conditions(conditions)
        return choice_class(**choice_dict)
    
    def _sub_parse_events(self, event_list):
        return [self._sub_parse_event(event) for event in event_list]
    
    def _sub_parse_event(self, event_dict):
        event_class = self.__load_class_from_module(interactions.events, event_dict.pop('type'))
        conditions = event_dict.pop('conditions', [])
        event_dict['conditions'] = self._sub_parse_conditions(conditions)
        return event_class(**event_dict)
    
    def _sub_parse_conditions(self, condition_list):
        return [self._sub_parse_condition(condition) for condition in condition_list]
    
    def _sub_parse_condition(self, condition_dict):
        condition_class = self.__load_class_from_module(interactions.conditions, condition_dict.pop('type'))
        return condition_class(**condition_dict)
    
    def _sub_parse_screens(self, screens_dict):
        return {sk: self._sub_parse_screen(screen_dict) for sk, screen_dict in screens_dict.items()}

    def _sub_parse_screen(self, screen_dict):
        return interactions.scene.Screen(**screen_dict)
    
    def _sub_parse_scenes(self, scenes_dict):
        return {sk: self._sub_parse_scene(scene_dict) for sk, scene_dict in scenes_dict.items()}

    def _sub_parse_scene(self, scene_dict):
        return interactions.thing.Thing(**scene_dict)
    
    @staticmethod
    def __load_class_from_module(module, class_name):
        if not hasattr(module, class_name):
            raise exceptions.LoadClassDoesNotExist(class_name)
        return getattr(module, class_name)

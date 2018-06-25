import os

this_file = os.path.realpath(__file__)
this_dir = os.path.dirname(this_file)
core_dir = this_dir
game_code = os.path.dirname(core_dir)
levels_dir = game_code + '/levels'

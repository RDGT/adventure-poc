from game_code.interactions import level
from game_code.levels.level_1 import outside


class level_2(level.Level):

    def get_first_scene(self):
        return outside.outside.run_scene(self.game)

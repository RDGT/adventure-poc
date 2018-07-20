import room
import level
import thing
from lib import scene
from lib import choices
from lib import area

# some constant scenes (mostly for testing)
the_end_lose = scene.Scene('Game Over', 'You lose')
the_end_win = scene.Scene('The End', 'You win')

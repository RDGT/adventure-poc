import room
import puzzle
import dialogue
import combat
from lib import scene

# some constant scenes (mostly for testing)
the_end_lose = scene.Scene('Game Over', 'You lose')
the_end_win = scene.Scene('The End', 'You win')

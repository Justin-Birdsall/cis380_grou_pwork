"""
This is the main game file that calls the other files. The logic is behind the game is to initialize all the 4 players of the game and while the game is not won -> continue to run turns until 1 player has 0 remaining tiles in hand or rack.
"""

import initialization_game
import game_turn
import tally_score

isgamewon = False
initialization_game()
while isgamewon != True:
    game_turn(isgamewon)
tally_score()


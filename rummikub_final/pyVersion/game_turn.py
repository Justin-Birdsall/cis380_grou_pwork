""" 
    The purpose of this file is to run through each players decision tree of playing
    sets and runs or drawing.
    Call the corresponding python functions according to said decision

    Note: 
"""
from initialization_game import players, board
from game_actions import *
from game_rules import *
def game_turn(gamewonflag):
    
    
    if(initial_30_flag(players) == False):
        draw_tile()
        board.turn += 1 
    elif(initial_30_flag(players)== True):
        #on that players turn check if they can make a play do it. Otherwise draw 
            if():
                pass
            else:
                draw_tile
    """ 
    If a player puts tile on the board  
    """
    if():
        pass
    #check if that player 
    return gamewonflag




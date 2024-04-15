"""  
This is the "meat of the program". This file is essentially a library of functions to call for each game turn based on the hand and the tiles that are in play. There may be some parts in this that are a little reductive like draw(). Drawing the tiles at the beginning of the game is slightly different than just playing and it is just makes more sense for my brain to create a drawing function separate from 
"""
import random
from initialization_game import players, board
#in the game turn file send the result of the seed % mod 
def initial_30_flag(player_list, board):
    if player_list[board.turn].sum_for_30 >=30:
        #take all playable sets and runs and do appropriate actions
        pass
    #check the bottom right hand corner 
    return(player_list)

def draw_tile(player_list, board):
    #add one random tile from 
    random.seed(board.seed) 
    
    return(player_list,board)

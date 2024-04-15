"""  
This is the "meat of the program". This file is essentially a library of functions to call for each game turn based on the hand and the tiles that are in play. There may be some parts in this that are a little reductive like draw(). Drawing the tiles at the beginning of the game is slightly different than just playing and it is just makes more sense for my brain to create a drawing function separate from 
"""
import random
from initialization_game import players, board
#in the game turn file send the result of the seed % mod 

def check_new_potential_sets(number, players, board):
    playernum = board.turn%4
    for j in range(4):
        if players[playernum].hand[j][number] > 0:
            count += 1
            sum += players[playernum].hand[j][number]
            color_of_tiles.append(j)
        if count >= 3:
            players[playernum].playable_set[number]=[color_of_tiles]
            players[playernum].sum_for_30 += sum
            count = 0   
            color_of_tiles = []         
        else:
        #players[playernum].set_potential[j]= players[playernum].hand[j][i]
            for color in color_of_tiles:
                players[playernum].set_potential[color].append(number)
            sum = 0
            count = 0
            color_of_tiles= []
    return(players,board)
def check_new_potential_run(color, players, board):
    playernum = [board.turn%4]
    for j in range(13):
        if players[playernum].hand[color][j] > 0:
        #if player.hand[i][j] > 0:
            count += 1
            #append to the list for the run
            #tile_nums.append(players[playernum].hand[i][j])
            #tile_nums.append((i,j))
            tile_nums.append(j)
        else:
            if count >= 3:
                # backtrack and add to buffer
                #for k in range(count, 0, -1):
                    #tile_nums.append((i, j-k))
                    #players[playernum].playable_run[i]=tile_nums
                players[playernum].playable_run[color].append(tile_nums)
                #players[playernum].playable_run[i][tile_nums[0]] = 1
                tile_nums = []
                count = 0
                
            else:
                #for tile in range(len(tile_nums)):
                k = len(tile_nums)
                for tile in tile_nums:    
                    #players[playernum].run_potential[tile[0]][tile[1]] = 1
                    #players[playernum].run_potential[i][tile] = 1
                    players[playernum].run_potential[color].append(tile)
                    #k -= 1
                    #player[playernum].run_potential[]= 
                    # NOTE: ^ may want to flip indices
                    
                    # V original
                    #players[playernum].run_potential[tile_nums[tile]][i] = 1
                tile_nums = []   
                count = 0   
    return(players,board)

def draw_tile(player_list, board):
    #add one random tile from 
    random.seed(board.seed) 
    while True:
            color = random.randint(0, 3)
            number = random.randint(0, 12)
            if board.pool[color][number] > 0:
                board.pool[color][number] -= 1
                players[board.turn%4].hand[color][number] += 1
                break
    check_new_potential_sets(number,players,board)
    check_new_potential_run(number,players,board)
    return(player_list,board)

def initial_30_flag(player_list, board):
    playernum = [board.turn%4]
    if player_list[playernum].sum_for_30 >=30:
    #check the bottom right hand corner
        if bool(player_list[playernum].playable_run):
            for i in range(4):
                for j in range(len(player_list[playernum].playable_run[i])):
                    if player_list[playernum].playable_run[i][j] in player_list[playernum].playable_set[i]:
                        for k in range(len(player_list[playernum].playable_run[i])):
                            sum1 += player_list[playernum].playable_run[i][k]
                        for k in range(len(player_list[playernum].playable_set[i])):
                            sum2 += player_list[playernum].playable_set[i][k]
                        if sum1 >= sum2:
                            choose run
                        else:
                            set
                            
                
    
        player_list[playernum].played_30 = True
    return(player_list)
""" 
This python file "gets the game ready to play".
In real life Rummikub can be played with 2-4 players.
We are only implementing a 4 player version of the game as it was
the easiest for us to understand from a mathematical and algorithm design perspective. In theory it shouldn't be too hard to make it 2 or 3 or 4 person
"""
import random

RED = 0
ORANGE = 1
BLUE = 2
BLACK = 3

class Joker:
    def __init__(self):
        self.joker0 = [-1][-1]
        self.joker1 = [-1][-1]
        self.joker0_on_board = False
        self.joker1_on_board = False    

class Board:
    def __init__(self, seed):
        colors = 4 #red, orange, blue, black
        numbers = 13 #1-13
        self.seed = seed
        self.turn = seed % 4
        self.pool = [[2 for i in range(numbers)] for j in range(colors)]      
        self.table_tiles = [[0 for i in range(numbers+1)] for j in range(colors+1)]
        self.table_sets = [[0 for i in range(numbers)] for j in range(colors)]
        self.table_runs = [[0 for i in range(numbers)] for j in range(colors)]

class Player:
    def __init__(self, name, num):
        self.name = name 
        self.num = num
        #self.hand = [[0] * 13 for _ in range(4)]
        self.hand = [[0 for _ in range(13)] for _ in range(4)]
        #self.run_potential = [[0] * 13 for _ in range(4)]
        #self.run_potential = [[0 for _ in range(13)] for _ in range(4)]
        self.run_potential = {i: [] for i in range(13)}
        self.set_potential = {i: [] for i in range(4)}
        self.playable_set = {i: [] for i in range(4)}
        self.playable_run = {i: [] for i in range(4)}
        self.played_30 = False
        self.sum_for_30 = 0
        self.joker_in_hand = 0

def init_draw(players, board):
    random.seed(board.seed)
    for i in range(56):
        while True:
            color = random.randint(0, 3)
            number = random.randint(0, 12)
            if board.pool[color][number] > 0:
                board.pool[color][number] -= 1
                players[board.turn%4].hand[color][number] += 1
                break
        board.turn += 1 
      

def check_hand_sets(players):
    #check if player has 3 or 4 of the same number (different colors)
    for playernum in range(len(players)):
        for i in range(13):
            count = 0
            sum = 0
            color_of_tiles =[]
            for j in range(4):
                if players[playernum].hand[j][i] > 0:
                    count += 1
                    sum += players[playernum].hand[j][i]
                    color_of_tiles.append(j)
            if count >= 3:
                #players[playernum].playable_set[i]=[color_of_tiles]
                #players[playernum].playable_set[color]=[color_of_tiles]
                k = len(color_of_tiles)
                for color in color_of_tiles:
                    players[playernum].playable_set[color].append(i)
                    k-=1
                
                players[playernum].sum_for_30 += sum
                count = 0   
                color_of_tiles = []         
            else:
                #players[playernum].set_potential[j]= players[playernum].hand[j][i]
                for color in color_of_tiles:
                    players[playernum].set_potential[color].append(i)
                sum = 0
                #
                count = 0
                color_of_tiles= []
                #playable_set[run start - run len] != run color
                
def check_hand_runs(players):
    for playernum in range(len(players)):
    #for playern in players:
        for i in range(4):
            count = 0
            runs = 0
            tile_nums = []
            for j in range(13):
                if players[playernum].hand[i][j] > 0:
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
                        players[playernum].playable_run[i].append(tile_nums)
                        #players[playernum].playable_run[i][tile_nums[0]] = 1
                        tile_nums = []
                        count = 0
                        
                    else:
                        #for tile in range(len(tile_nums)):
                        k = len(tile_nums)
                        for tile in tile_nums:    
                            #players[playernum].run_potential[tile[0]][tile[1]] = 1
                            #players[playernum].run_potential[i][tile] = 1
                            players[playernum].run_potential[i].append(tile)
                            #k -= 1
                            #player[playernum].run_potential[]= 
                            # NOTE: ^ may want to flip indices
                            
                            # V original
                            #players[playernum].run_potential[tile_nums[tile]][i] = 1
                        tile_nums = []   
                        count = 0                        

# test main
if __name__ == "__main__":
    board = Board(random.randint(0,99999))
    player1 = Player("player1", 0)    
    player2 = Player("player2", 1)     
    player3 = Player("player3", 2)    
    player4 = Player("player4", 3)
    players = [player1,player2,player3,player4]
    init_draw(players,board)
    check_hand_runs(players)
    check_hand_sets(players)
    
    
    print("Board pool")
    for i in range(4):
        print(board.pool[i])
    print()
    print("Player 1 hand")
    for i in range(4):
        print(player1.hand[i])
    print("Player 1 playable run")
    for i in range(4):
        print(player1.playable_run[i])
    print("Player 1 potential run")
    for i in range(4):
        print(player1.run_potential[i])
    print("Player 1 playable set")
    for i in range(4):
        print(player1.playable_set[i])
    print("Player 1 potential set")
    for i in range(4):
        print(player1.set_potential[i])
    print()
    print("Player 2 hand")
    for i in range(4):
        print(player2.hand[i])
    print("Player 2 playable run")
    for i in range(4):
        print(player2.playable_run[i])
    print("Player 2 potential run")
    for i in range(4):
        print(player2.run_potential[i])
    print("Player 2 playable set")
    for i in range(4):
        print(player2.playable_set[i])
    print("Player 2 potential set")
    for i in range(4):
        print(player2.set_potential[i])
    print()
    print("Player 3 hand")
    for i in range(4):
        print(player3.hand[i])
    print("Player 3 playable run")
    for i in range(4):
        print(player3.playable_run[i])
    print("Player 3 potential run")
    for i in range(4):
        print(player3.run_potential[i])
    print("Player 3 playable set")
    for i in range(4):
        print(player3.playable_set[i])
    print("Player 3 potential set")
    for i in range(4):
        print(player3.set_potential[i])
    print()
    print("Player 4 hand")
    for i in range(4):
        print(player4.hand[i])
    print("Player 4 playable run")
    for i in range(4):
        print(player4.playable_run[i])
    print("Player 4 potential run")
    for i in range(4):
        print(player4.run_potential[i])
    print("Player 4 playable set")
    for i in range(4):
        print(player4.playable_set[i])
    print("Player 4 potential set")
    for i in range(4):
        print(player4.set_potential[i])
        
    
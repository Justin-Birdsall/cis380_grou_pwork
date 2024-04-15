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
        self.hand = [[0] * 13+1 for _ in range(4+1)]
        self.run_potential = [[0] * 13 for _ in range(4)]
        self.set_potential = {i: [] for i in range(4)}
        self.playable_set = {i: [] for i in range(13)}
        self.playable_set = {i: [] for i in range(4)}
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
    for playernum in players:
        for i in range(13):
            count = 0
            sum = 0
            color_of_tiles=[]
            for j in range(4):
                if players[playernum].hand[j][i] > 0:
                    count += 1
                    sum += players[playernum].hand[j][i]
                    color_of_tiles.append(j)                    
                else:
                    players[playernum].set_potential[j]= players[playernum].hand[j][i]
            if count >= 3:
                players[playernum].playable_set[i]=[color_of_tiles]
                players[playernum].sum_for_30 += sum
                
def check_hand_runs(players):
    for playernum in players:
        for i in range(4):
            count = 0
            runs = 0
            tile_nums = []
            for j in range(13):
                if players[playernum].hand[i][j] > 0:
                    count += 1
                    #append to the list for the run
                    tile_nums.append(players[playernum].hand[i][j])
                if count >= 3:
                    players[playernum].playable_run[j]=tile_nums
                else:
                    for tile in range(len(tile_nums)):
                        players[playernum].run_potential[tile_nums[tile]][i] = 1
                    tile_nums = []   
                    count = 0
                    
board = Board(random.randint(0,99999))
player1 = Player("player1", 0)    
player2 = Player("player2", 1)     
player3 = Player("player3", 2)    
player4 = Player("player4", 3)
players = [player1,player2,player3,player4]
init_draw(players,board)
check_hand_runs(players)
check_hand_sets(players)





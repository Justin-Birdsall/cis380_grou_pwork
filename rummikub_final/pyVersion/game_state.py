import random

RED = 0
ORANGE = 1
BLUE = 2
BLACK = 3

class GameState:
    def __init__(self):
        colors = 4 #red, orange, blue, black
        numbers = 13 #1-13
        self.pool = [[2 for i in range(numbers)] for j in range(colors)]      
        self.table = [[0 for i in range(numbers)] for j in range(colors)]
        self.sets = [[0 for i in range(numbers)] for j in range(colors)]
        self.runs = [[0 for i in range(numbers)] for j in range(colors)]
        self.player1_hand = [[0 for i in range(numbers)] for j in range(colors)]
        self.player2_hand = [[0 for i in range(numbers)] for j in range(colors)]
        self.player3_hand = [[0 for i in range(numbers)] for j in range(colors)]
        self.player4_hand = [[0 for i in range(numbers)] for j in range(colors)]

    # playernum is bugged in syntax highlighting, it's fine
    def draw(self, playernum):
        # draw random tile from pool, 
        while True:
            color = random.randint(0, 3)
            number = random.randint(0, 12)
            if self.pool[color][number] > 0:
                self.pool[color][number] -= 1
                # swapcase 
                if playernum == 1:
                    self.player1_hand[color][number] += 1
                elif playernum == 2:
                    self.player2_hand[color][number] += 1
                elif playernum == 3:
                    self.player3_hand[color][number] += 1
                elif playernum == 4:
                    self.player4_hand[color][number] += 1
                break
        
    def check_hand_sets(self, playernum):
        # check if player has 3 or 4 of the same number (different colors)
        for i in range(13):
            count = 0
            for j in range(4):
                if playernum == 1:
                    if self.player1_hand[j][i] > 0:
                        count += 1
                elif playernum == 2:
                    if self.player2_hand[j][i] > 0:
                        count += 1
                elif playernum == 3:
                    if self.player3_hand[j][i] > 0:
                        count += 1
                elif playernum == 4:
                    if self.player4_hand[j][i] > 0:
                        count += 1
            if count >= 3:
                #for j in range(4):
                if playernum == 1:
                    print("Player 1 has a set of number ", i+1)
                elif playernum == 2:
                    print("Player 2 has a set of number ", i+1)
                elif playernum == 3:
                    print("Player 3 has a set of number ", i+1)
                elif playernum == 4:
                    print("Player 4 has a set of number ", i+1)
                # testing, add set to table
                for num in range(4):
                    if playernum == 1:
                        if self.player1_hand[num][i] > 0:
                            self.player1_hand[num][i] -= 1
                            self.table[num][i] += 1
                    elif playernum == 2:
                        if self.player2_hand[num][i] > 0:
                            self.player2_hand[num][i] -= 1
                            self.table[num][i] += 1
                    elif playernum == 3:
                        if self.player3_hand[num][i] > 0:
                            self.player3_hand[num][i] -= 1
                            self.table[num][i] += 1
                    elif playernum == 4:
                        if self.player4_hand[num][i] > 0:
                            self.player4_hand[num][i] -= 1
                            self.table[num][i] += 1

    
    


if __name__ == "__main__":
    game = GameState()
    print("Pool")
    print(game.pool)
    #game.pool[BLUE][13-1] = 0
    print()
    #game.draw(1)
    for i in range(14):
        game.draw(1)
        game.draw(2)
        game.draw(3)
        game.draw(4)
    print("Pool")
    print(game.pool)
    print()
    print("Player 1 Hand")
    print(game.player1_hand)
    print()
    print("Player 2 Hand")
    print(game.player2_hand)
    print()
    print("Player 3 Hand")
    print(game.player3_hand)
    print()
    print("Player 4 Hand")
    print(game.player4_hand)
    print()
    game.check_hand_sets(1)
    game.check_hand_sets(2)
    game.check_hand_sets(3)
    game.check_hand_sets(4)
    print()
    print("Table")
    print(game.table)
    print()
    print("Player 1 Hand")
    print(game.player1_hand)
    print()
    print("Player 2 Hand")
    print(game.player2_hand)
    print()
    print("Player 3 Hand")
    print(game.player3_hand)
    print()
    print("Player 4 Hand")
    print(game.player4_hand)
    print()
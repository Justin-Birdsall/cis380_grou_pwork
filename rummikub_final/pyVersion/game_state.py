import random

RED = 0
ORANGE = 1
BLUE = 2
BLACK = 3

# transfered to init file
class Player:
    def __init__(self, num):
        colors = 4 #red, orange, blue, black
        numbers = 13 #1-13
        self.num = num
        self.hand = [[0 for i in range(numbers)] for j in range(colors)]
        self.potential_sets = [[0 for i in range(numbers)] for j in range(colors)]
        self.potential_runs = [[0 for i in range(numbers)] for j in range(colors)]
    
    def draw(self, board):
        # draw random tile from pool
        while True:
            color = random.randint(0, 3)
            number = random.randint(0, 12)
            if board.pool[color][number] > 0:
                board.pool[color][number] -= 1
                self.hand[color][number] += 1
                break
    
    def check_hand_sets(self):
        # check if player has 3 or 4 of the same number (different colors)
        for i in range(13):
            count = 0
            set_buffer = []
            for j in range(4):
                if self.hand[j][i] > 0:
                    count += 1
                    set_buffer.append((j, i))
            if count >= 3:
                # testing print
                print("Player ", self.num, " has a set of number ", i+1)
                # add to potential sets
                for pair in set_buffer:
                    self.potential_sets[pair[0]][pair[1]] += 1
    
    def check_hand_runs(self):
        for i in range(4):
            count = 0
            runs = 0
            run_buffer = []
            for j in range(13):
                if self.hand[i][j] > 0:
                    count += 1
                    if count == 3:
                        runs += 1
                else:
                    if count >= 3:
                        # backtrack and add to buffer
                        for k in range(count, 0, -1):
                            run_buffer.append((i, j-k))
                    count = 0
            # if there are runs up to the end, add to buffer
            if count >= 3:
                for k in range(count, 0, -1):
                    run_buffer.append((i, 13-k))
            if runs > 0:
                # testing print
                print("Player ", self.num, " has ", runs, " run(s) of color ", i)
                for pair in run_buffer:
                    self.potential_runs[pair[0]][pair[1]] += 1
    
    def play_sets(self, board):
        pass

    def play_runs(self, board):
        pass

    #TODO: implement table that has xor of sets and runs    - no conflicts
    #TODO: implement table that has xor of (sets and runs) and hand - tiles not in sets or runs
    
    #TODO: branching:
    #BRANCHING: 1. Do we have potential sets, runs, or individual tiles to play?
    #               - If yes, go to BRANCHING 2
    #               - If no, draw a tile
    #BRANCHING: 2. Do we have conflicts with sets and runs? TODO: how do individual tiles play into this?
    #               - If yes, go to RECURSION 1, but first? do individual tiles
    #               - If no, play the sets and runs, and individual tiles
    #RECURSION: 1. Set/Run conflict resolution, Set inclusion/exclusion, (ran on all sets)
    #               - XOR sets and runs with sets to get conflicts and and it with sets to get the "ghost" of the set and its "remains"
    #               - Do something to restore the conflicted sets to a non-broken state
    
    
    
    
    
    #               - Choose first set
    #                   - Include
    #                       - Did this cause a conflict?
    #                           - If yes, compare this branch with the exclusion branch
    #                               - Go to RECURSION 2
    #                           - If no, go to the next set
    #                   - Exclude
    #                       - Did this resolve the (a?) conflict?
    #                           - If yes, compare this branch with the inclusion branch
    #                               - Go to RECURSION 2
    #                           - If no, go to the next set
    #RECURSION: 2. Set/Run conflict resolution, Run inclusion/exclusion, (ran on all runs)
    #               - Choose first run
    #                   - Include
    #                       - Did this cause a conflict?
    #                           - If yes, compare this branch with the exclusion branch
    #                               - Go to RECURSION 3
    #                           - If no, go to the next run
    #                   - Exclude
    #                       - Did this resolve the (a?) conflict?
    #                           - If yes, compare this branch with the inclusion branch
    #                               - Go to RECURSION 3
    #                           - If no, go to the next run
    #RECURSION: 3. Just choose Sets.
                        
# transfered to init file
class GameState:
    def __init__(self):
        colors = 4 #red, orange, blue, black
        numbers = 13 #1-13
        self.pool = [[2 for i in range(numbers)] for j in range(colors)]      
        self.table = [[0 for i in range(numbers)] for j in range(colors)]
        self.sets = [[0 for i in range(numbers)] for j in range(colors)]
        self.runs = [[0 for i in range(numbers)] for j in range(colors)]

# testing
if __name__ == "__main__":
    game = GameState()
    player_1 = Player(1)
    player_2 = Player(2)
    player_3 = Player(3)
    player_4 = Player(4)
    
    # draw 14 tiles for each player
    for i in range(14):
        player_1.draw(game)
        player_2.draw(game)
        player_3.draw(game)
        player_4.draw(game)
    
    # value checks
    print("Player 1 Hand")
    for i in range(4):
        print(player_1.hand[i])
    player_1.check_hand_sets()
    player_1.check_hand_runs()
    print("Player 1 Potential Sets")
    for i in range(4):
        print(player_1.potential_sets[i])
    print("Player 1 Potential Runs")
    for i in range(4):
        print(player_1.potential_runs[i])
        
    print()
    print("Player 2 Hand")
    for i in range(4):
        print(player_2.hand[i])
    player_2.check_hand_sets()
    player_2.check_hand_runs()
    print("Player 2 Potential Sets")
    for i in range(4):
        print(player_2.potential_sets[i])
    print("Player 2 Potential Runs")
    for i in range(4):
        print(player_2.potential_runs[i])
    
    print()
    print("Player 3 Hand")
    for i in range(4):
        print(player_3.hand[i])
    player_3.check_hand_sets()
    player_3.check_hand_runs()
    print("Player 3 Potential Sets")
    for i in range(4):
        print(player_3.potential_sets[i])
    print("Player 3 Potential Runs")
    for i in range(4):
        print(player_3.potential_runs[i])
    
    print()
    print("Player 4 Hand")
    for i in range(4):
        print(player_4.hand[i])
    player_4.check_hand_sets()
    player_4.check_hand_runs()
    print("Player 4 Potential Sets")
    for i in range(4):
        print(player_4.potential_sets[i])
    print("Player 4 Potential Runs")
    for i in range(4):
        print(player_4.potential_runs[i])
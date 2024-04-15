""" 
I would consider this to be a part of the game_rules/actions.py since it's essentially another library of functions for the game_turn to call. The thing is jokers add a layer of complexity to the game that trying to put all the logic into the game_rules.py file makes the problem a little harder to think about. The functions should modify how the joker acts. It shouldn't mess with too much of the logic of "makable plays". If players have "access" to using the joker then it opens up the possibility of what they can do with their hand (filling in a gap)
"""

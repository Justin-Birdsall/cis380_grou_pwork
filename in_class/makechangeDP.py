# tabulation, 


def exact_change(x, coins):
    if x == 0:
        return 0
    if all([x < coin for coin in coins]):
        return None
    options = []
    for coin in coins:
        num_coins = exact_change(x - coin, coins)
        if num_coins is None:
            continue
        options.append(num_coins + 1)
    return None if len(options) == 0 else min(options)




def thing(total, coins):
    dp_table = [0][0]
    # total % biggest coin that fits

    # if total % coin == total #does not fit
    #row is the number of coins that we are given to make change with +1
    row = 0
    col = 1
    for coin in coins:
        if total % coin == total:
            #if we can't use that coin no point in creating a table for it
            row -= 1
            break
        else:
            #dp_table[][]
            row =
            col = 
            for i in range(row):
                dp_table[i][i]
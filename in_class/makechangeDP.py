import math

def make_change(change_to_make, coins):
    change_dict = {coin: 0 for coin in coins}

    if 1 in coins:
        pennies = True
        coins.remove(1)
    else:
        pennies = False
        
    coins = [coin for coin in coins if coin <= change_to_make]
    rows = len(coins) + 1

    max_coin = max(coins) if coins else 1
    cols = math.ceil(change_to_make / max_coin) + 1

    dp = [[0] * cols for _ in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
		if j - coins[i-1] >= 0:
		    dp[i][j] = max(dp[i-1][j], dp[i][j-coins[i-1]] + 1)
		else:
		    dp[i][j] = dp[i-1][j]
    change = change_to_make
    for i in range(rows - 1, 0, -1):
        for j in range(cols - 1, 0, -1):
            while dp[i][j] > 0:
                change_dict[coins[i-1]] += 1
                change -= coins[i-1]
                dp[i][j] -= 1

    if pennies:
        pennies_needed = change
        change_dict[1] = pennies_needed
        change -= pennies_needed

    if change != 0:
        print("Change cannot be made.")
    else:
        print("Change made successfully.")
    
    print("Coins used:")
    for coin, count in change_dict.items():
        print(f"{coin}: {count}")

# Example usage:
make_change(15, [5, 10, 25])  # Change for 15 cents using nickels, dimes, and quarters

def exact_change(x, coins):
    
    > 0
if __name__ == "__main__":
    #ask user for the change that we hvae to make
    change_to_hand_back = int(input())
    #ask user for what coins we have access to
    coins = list(map(int, input().split()))
    print(coins)
    exact_change(change_to_hand_back, coins)

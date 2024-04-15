import heapq
def make_change(coins, value):
    retlist = []
    #base case
    if value == 0:
        return retlist
     #recurse case
    else:
        # general recurse



        # change to return a list of lists, with each list being a possible combination of coins
        # except it's cringe and wouldn't work with recursion easily so i give up
        
        for coin in coins:
            #print(coin)
            if value - int(coin) >= 0:
                #heapq.heappush(retlist,)
                #return [int(coin)].extend(make_change(coins, value - int(coin)))
                if make_change(coins, value - int(coin)) != None:
                    retlist.append(int(coin))
                    retlist.extend(make_change(coins, value - int(coin)))
                else:
                    retlist.append(int(coin))
                    return retlist

if __name__ == "__main__":
    #ask the user for the value of change to make should be int no?
    change_we_have_access_to = input().split()
    change_to = int(input().split()[0])
    print(make_change(change_to_make, coins_worth)
    #print(coins)
    #print(value)


                
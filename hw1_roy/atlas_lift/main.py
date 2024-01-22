# Authors: Richard Roy
#          Justin 
# References: https://stackoverflow.com/questions/4663306/get-a-list-of-numbers-as-input-from-the-user
#             https://stackoverflow.com/questions/1207406/how-to-remove-items-from-a-list-while-iterating

if __name__ == "__main__":
    num_contestants = int(input())

    str_list = input().split()
    contestant_times = [int(i) for i in str_list]

    sec = 0

    print(len(contestant_times))
    
    contestants_left = len(contestant_times)

    while len(contestant_times) > 0:
        contestant_times[:] = [contestant for contestant in contestant_times if contestant != sec]
        # ^ 2nd source, "remakes" the list in-place without the contestants who just failed
        if len(contestant_times) < contestants_left:
            contestants_left = len(contestant_times)
            if contestants_left != 0:
                print(contestants_left)
        sec += 1
        

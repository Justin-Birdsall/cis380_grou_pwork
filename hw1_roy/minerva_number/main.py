# Author: Richard Roy

# Date 1/12/2024



from math import sqrt

from math import floor

from math import ceil

if __name__ == "__main__":

    num_tests = int(input())

    

    for test_idx in range(num_tests):

        test = input().split()

        x,y,d,s,b = int(test[0]),int(test[1]),0,0,0

        perfect_list = [i*i for i in range(ceil(sqrt(x)),floor(sqrt(y))+1)]

        first_12 = 0

        last_12 = 0

        for i in range(x,y+1):

            if i % 12 == 0:

                first_12 = i

                break

        for i in range(y,x-1,-1):

            if i % 12 == 0:

                last_12 = i

                break



        if first_12 == 0:

            d = 0

        else:

            if first_12 == last_12:

                d = 1

            else:

                d = floor(last_12/12 - first_12/12 + 1) # + 1, otherwise it excludes the first 12 here, floor to change to int

        

        for num in perfect_list:

            if num % 12 == 0:

                b += 1



        s = len(perfect_list)  

            

        print(d,s,b)
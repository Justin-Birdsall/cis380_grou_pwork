# Authors: Richard Roy
#          Justin Birdsall


from math import floor
if __name__ == "__main__":
    num_tests = int(input())
    

    for test_idx in range(num_tests):
        test = input().split()
        x = int(test[0])
        y = int(test[1])
        n = int(test[2])

        retList = []
        
        it_n = n
        while it_n >= floor(n/2):
            distance = 0
            distance += it_n * x
            distance += (n - it_n) * y
            retList.append(distance)
            distance = 0
            distance += it_n * y
            distance += (n - it_n) * x
            retList.append(distance)
            it_n -= 1



        
        retList = list(set(retList))
        retList.sort()
        print(*retList)


    
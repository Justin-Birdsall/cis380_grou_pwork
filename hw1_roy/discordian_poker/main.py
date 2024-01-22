if __name__ == "__main__":
    num_tests = int(input())

    for test_idx in range(num_tests):
        line = input().split()
        S = int(line[0]) # Starting bet
        k = int(line[1]) # Number of rounds

        # Your code goes here!
        for k in range(k, 0, -1):
            if S % 2 == 0:
                S = S - 99
                S = S * 3
            else:
                S = S - 15
                S = S * 2
            if S % 1000000 != 0:
                S = S % 1000000
            while S < 0:
                S = 1000000 - abs(S)
        print(S)
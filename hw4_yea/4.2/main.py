# Authors: Richard Roy, Justin Birdsall
# Referenced: https://www.youtube.com/watch?v=jlCJqgSgXI4


if __name__ == "__main__":
    num_tests = int(input())
    for i in range(num_tests):
        num_brick_types, max_power = map(int, input().split())
        brick_types = list(map(int, input().split()))
        brick_types.sort()
        #dp_table = [0] * (max_power + 1)
        dp_table = [[0 for _ in range(max_power + 1)] for _ in range(num_brick_types + 1)]
        for j in range(1, max_power + 1): # columns
            for k in range(1, num_brick_types + 1): # rows
                # if j - dp_table[k][j-1] >= brick_types[k-1]:  # check if this type of brick "fits"
                #     dp_table[k][j] = dp_table[k][j-1] + brick_types[k-1]  # no longer 0 at this spot, becomes a contender for final value
                # dp_table[k][j] = max(dp_table[k-1][j], dp_table[k][j-1], dp_table[k][j])
                if j - brick_types[k-1] >= 0: # if the brick fits using the current brick
                    #dp_table[k][j] = max(dp_table[k-1][j], dp_table[k][j-1], dp_table[k-1][j - brick_types[k-1]] + brick_types[k-1]) # max of the three options (previous row, previous column, or previous row and column) 
                    dp_table[k][j] = max(dp_table[k-1][j], dp_table[k][j-1], dp_table[k-1][j - brick_types[k-1]] + brick_types[k-1])
                else: # if the brick doesn't fit
                    #dp_table[k][j] = max(dp_table[k-1][j], dp_table[k][j-1])
                    # check if not previously using another brick type is better
                    #for
                
        
        
        
        
        #print(dp_table)
        print("Answer:")
        print(dp_table[num_brick_types][max_power])
        print("Table:")
        print(dp_table)
        print("Brick Types:")
        print(brick_types)
        print("Max Power:")
        print(max_power)
                




                #if j - brick_types[k] >= 0:
                    #dp_table[k][j] = max(dp_table[k - 1][j], dp_table[k - 1][j - brick_types[k]] + brick_types[k])
                    #dp_table[k][j] = max(dp_table[k-1][j], dp_table[k][j-1])
                    #dp_table[k][j] = max(dp_table[k-1][j], dp_table[k][j-1])





                #if j - brick_types[k] >= 0:
                #dp_table[k][j] = max(dp_table[k - 1][j], dp_table[k - 1][j - brick_types[k]] + brick_types[k])
                    #dp_table[j] = max(dp_table[j], dp_table[j - brick_types[k]] + brick_types[k])



# need to factor in using multiple different brick types
# need to factor in using the same brick type multiple times
# need to factor in not using a brick type at all

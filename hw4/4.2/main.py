# Authors: Richard Roy, Justin Birdsall


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
                if j - dp_table[k][j-1] >= brick_types[k-1]:  # check if this type of brick "fits"
                    dp_table[k][j] = dp_table[k][j-1] + brick_types[k-1]  # no longer 0 at this spot, becomes a contender for final value
                dp_table[k][j] = max(dp_table[k-1][j], dp_table[k][j-1], dp_table[k][j])
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

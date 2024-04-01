# Authors: Richard Roy, Justin Birdsall
# Referenced: https://www.youtube.com/watch?v=jlCJqgSgXI4

# dictionary cache for memoization
cache = {}
def max_power_func(brick_types, max_power, i):
    global cache
    if len(brick_types) == 0:
        return 0
    #cache = {}
    if max_power in cache:
        return cache[max_power]
    #for brick in brick_types:
    #for brick in brick_types[i:]:
    if i == len(brick_types):
        #i = 0
        return 0
    brick = brick_types[i]
    if brick <= max_power:
        #return max_power(brick_types, max_power - brick) + brick
        #include_brick = max_power(brick_types, max_power - brick, cache, i) + brick
        #exclude_brick = max_power(brick_types, max_power, cache, i+1)

        #include_brick = (max_power_func(brick_types, max_power - brick, i) + brick)
        if max_power - brick in cache:
            include_brick = cache[max_power - brick] + brick
        else:
            include_brick = (max_power_func(brick_types, max_power - brick, i) + brick)
        exclude_brick = (max_power_func(brick_types, max_power, i+1))

        cache[max_power] = max(include_brick, exclude_brick)
        return cache[max_power]
    else:
        #return 0, {} 
        return 0
        
#def max_power_helper(brick_types, max_power):

if __name__ == "__main__":
    num_tests = int(input())
    for i in range(num_tests):
        cache = {}
        num_brick_types, max_power = map(int, input().split())
        brick_types = list(map(int, input().split()))
        brick_types.sort()
        # accounting for bricks of size 1 and 2 (easily calculable, to avoid unnecessary recursion)
        if 1 in brick_types:
            print(max_power) # if there is a brick of size 1 any positive integer can be reached
        # elif 2 in brick_types:
        #     # remove 2 from list
        #     brick_types.remove(2)
        #     no_twos = max_power_func(brick_types, max_power, 0)
        #     # if max_power is even and greater than 0, any is possible
        #     if max_power % 2 == 0 and max_power > 0:
        #         print(max_power)
        #     else:
        #         # if max_power is odd, check if no_twos + 2 is greater than max_power
        #         #if no_twos + 2 < max_power:
        #         #    twos_append = no_twos + 2
        #         #    while twos_append < max_power:
        #         #        twos_append += 2
                
        #         #if no_twos is odd, and no_twos + 2 is less than max_power, any is possible
        #         if no_twos % 2 == 1 and no_twos + 2 < max_power:
        #             print(max_power)
        #         elif no_twos % 2 == 0 and no_twos + 2 == max_power:
        #             print(max_power)
        #         else:
        #             #print(no_twos)
        #             # we should be able to reach 1 less than max_power because it is even
        #             print(max_power - 1)
        else:
            print(max_power_func(brick_types, max_power, 0))
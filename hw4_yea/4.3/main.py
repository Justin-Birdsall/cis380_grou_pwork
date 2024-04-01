# Authors: Richard Roy, Justin Birdsall

# Authors: Richard Roy, Justin Birdsall
# Referenced: https://www.youtube.com/watch?v=jlCJqgSgXI4

# dictionary cache for memoization
cache = {}
combos = []
def possible_combinations(brick_types, target_length, i, current_combo):
    global cache
    global combos
    if len(brick_types) == 0:
        return 0
    if i == len(brick_types): #only loop through brick_types once (find combinations of bricks without ordering, will mathematically cover all combinations later)
        return 0
    brick = brick_types[i]
    if brick == target_length:
        combos.append(current_combo.append(brick))
        return 1
    #if brick < target_length:
    if target_length - brick >= 0:
        if target_length - brick in cache:
            include_brick = cache[target_length - brick]
        else:
            include_brick = possible_combinations(brick_types, target_length - brick, i, current_combo.append(brick))
        exclude_brick = possible_combinations(brick_types, target_length, i+1, current_combo)
        cache[target_length] = include_brick + exclude_brick
        return cache[target_length]
    else:
        return 0


if __name__ == "__main__":
    num_tests = int(input())
    for i in range(num_tests):
        cache = {}
        combos = []
        num_brick_types, target_length = map(int, input().split())
        brick_types = list(map(int, input().split()))
        brick_types.sort()
        print(possible_combinations(brick_types, target_length, 0, []))

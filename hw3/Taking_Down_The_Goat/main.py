# Authors: Richard Roy, Justin Birdsall

if __name__ == "__main__":
    # first line: N number of tubes (0 - N-1)
    # and K number of tubes to explode 

    # the next K values: indicate the tube numbers to explode

    # output: a single int that is the distance from the clostest explosion
    # ^^ farthest distace from any explosion, but the val is the distance from the closest explosion
    # ^^^ best distance possible

    input_line = input().split()
    num_tubes = int(input_line[0])
    num_exploding = int(input_line[1])

    # get the tubes to explode
    tubes_to_explode = input().split()

    # PLAN: sort the tubes to explode, then find the best distance between tubes
    tubes_to_explode.sort()

    # TODO: come up with logic to find the best distance between tubes
    # while keeping the amount of tubes not exploding in mind
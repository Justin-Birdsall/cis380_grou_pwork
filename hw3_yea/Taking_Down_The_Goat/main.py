# Authors: Richard Roy, Justin Birdsall
from math import floor
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
    # convert to int
    tubes_to_explode = list((int(i) for i in tubes_to_explode))

    # PLAN: sort the tubes to explode, then find the best distance between tubes
    tubes_to_explode.sort()

    # TODO: come up with logic to find the best distance between tubes
    # while keeping the amount of tubes not exploding in mind


    # get the distance between all exploding tubes
    # find the best distance between tubes
    # print the middle distance between tubes

    # get the distance between all exploding tubes
    # each tube 

    # make each exploding tube a key in a dictionary

    # greatest distance between tubes (tuple)
    # make sure to account for no or one exploding tube
    exploding_tube_distances = {}

    # TODO: not working for last exploding to last non-exploding
    if len(tubes_to_explode) == 1:
        if tubes_to_explode[0] < num_tubes / 2:
            # print the distance from the first exploding tube to the end
            print(num_tubes -1 - tubes_to_explode[0])
        else:
            # print the distance from the first tube to the first exploding tube
            print(tubes_to_explode[0])
    else:
        # dictionary of "neighboring" exploding tubes
        # where key is the tuple of two "neighboring" exploding tubes

        # and the value is the distance between the two tubes
        tube_iterator = 0
        # tuple of tubes to explode
        tube_pair = []
        max_distance = -1
        for tube in tubes_to_explode:
            # never reached w/ 2 tubes
            if tube_iterator == 2:
                tube_iterator = 0
                # push pair to dictionary

                #exploding_tube_distances[tube_pair] = (tube_pair[1] - tube_pair[0])
                #if exploding_tube_distances[tube_pair] > max_distance:
                #    max_distance = exploding_tube_distances[tube_pair]
                if tube_pair[1] - tube_pair[0] > max_distance:
                    max_distance = tube_pair[1] - tube_pair[0]
                    # test print

                # reset tube_pair
                tube_pair = []
                tube_pair.append(tube)
                tube_iterator += 1
            else:
                #tube_pair += int(tube)
                if tube_iterator == 0:
                    #tube_pair[0] = int(tube)
                    tube_pair.append(tube)
                
                else:
                    #tube_pair[1] = int(tube)
                    tube_pair.append(tube)
                tube_iterator += 1
            #TODO: this is indented too far, but it fucks it up if I fix it, other issues too    
            # if anything is in tube_pair (full pair) only relevant if 2 tubes only
            if len(tube_pair) == 2:
                if tube_pair[1] - tube_pair[0] > max_distance:
                    max_distance = tube_pair[1] - tube_pair[0]
                    print("does this change our max?")


            # check if the greatest distance between exploding tubes is
            # greater than the distance from the first tube to the first exploding tube
            # or the distance from the last exploding tube to the last tube
            # TODO: ^
            if tubes_to_explode[0] == 0:
                # first tube is exploding, so the distance from the first tube to the first exploding tube is 0
                pass
            elif tubes_to_explode[0] - 0 > max_distance:
                # * 2 because the distance is from non-exploding tube to exploding tube
                # and we are converting from exploding tube to exploding tube
                # this effectively places the non-exploding tube in the middle of the exploding tube
                # and a non-exisitent exploding tube
                max_distance = (tubes_to_explode[0] - 0) * 2
            if tubes_to_explode[len(tubes_to_explode) - 1] == num_tubes - 1:
                # last tube is exploding, so the distance from the last tube to the last exploding tube is 0
                pass
            elif num_tubes - 1 - tubes_to_explode[len(tubes_to_explode) - 1] > max_distance:
                # see above for explanation of * 2
                max_distance = (num_tubes - 1 - tubes_to_explode[len(tubes_to_explode) - 1]) * 2

            print(num_tubes - 1 - tubes_to_explode[len(tubes_to_explode) - 1])
            

        
        # divide the max distance by 2
        print(floor(max_distance / 2))
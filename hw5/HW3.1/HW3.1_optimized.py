# Authors: Richard Roy & Justin Birdsall


# plan: use maxheap so we can just pop the max value off
# for however many missions we want to foil

# that way we don't have to sort the list of missions at all

# or just use quicksort or mergesort to sort the list of missions
# ^ trying this first for simplicity
import cProfile
import timeit

if __name__ == "__main__":
    input_line = input().split()
    num_missions = int(input_line[0])
    num_foil = int(input_line[1])
    mission_list = []
    # input_line[0] is the number of missions
    # input_line[1] is the number of missions to foil
    
    #for i in range(num_missions):
    #    mission_list.append(int(input().split()[0]))
    {mission_list.append(int(input().split()[0])) for i in range(num_missions)}

    # sort the list of missions
    mission_list.sort()
    # print top num_foil missions
    #for i in range(num_foil):
    #    print(mission_list.pop())
    {print(mission_list.pop()) for i in range(num_foil)}
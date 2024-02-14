# Authors: Richard Roy
#          Justin Birdsall


from math import floor
if __name__ == "__main__":
    num_tests = int(input())
 

    for test_idx in range(num_tests):
        test = input().split()
        n = int(test[0])        #starting gallons
        m = int(test[1])        #gals needed to fill one cell (travel 1 mile)
        c = int(test[2])        #empty cells needed to make a new cell

        distance_traveled = 0
        fuel_cells = 0
        empty_cells = 0

        fuel_cells = floor(n/m)

        distance_traveled += fuel_cells
        empty_cells = fuel_cells
        fuel_cells = 0

        while empty_cells >= c:
            fuel_cells += floor(empty_cells/c)
            empty_cells = empty_cells%c
            distance_traveled += fuel_cells
            empty_cells += fuel_cells
            fuel_cells = 0

        print(distance_traveled)

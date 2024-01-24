# Authors: Richard Roy
#          Justin 
# References: https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/

if __name__ == "__main__":
    x_y_count = int(input())
    row_count = x_y_count[0]
    grid = []
    for i in range(row_count):
        row = input().split()
        grid.append(row)



    score = 0
    
    def check_space(x, y, r, c):
        if x <= 0 or y <= 0:
            return False
        if x >= len(r) or y >= len(c):
            return False
        if r[x] == 'B' 
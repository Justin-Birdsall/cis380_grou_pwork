# Authors: Richard Roy, Justin Birdsall

# satellite node class
class Satellite:
    def __init__(self, index, data, energy, parent):
        self.index = index
        self.data = data
        self.energy = energy
        self.parent = parent
        self.children = []

if __name__ == "__main__":
    num_sats = int(input())
    sat_list = []
    for i in range(num_sats):
       sat_list.append(input().split()) 
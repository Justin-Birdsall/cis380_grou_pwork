

if __name__ == "__main__":
    stack = []
    # add initial state to stack
    stack.append((1, 2, 3, 4, 5, 6, 7, 8))
    first, second, third, fourth, fifth, sixth, seventh, eighth = stack.pop()
    # while stack is not empty
    print(first, second, third, fourth, fifth, sixth, seventh, eighth)
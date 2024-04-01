def calculate_median(fifo_list):
    n = len(fifo_list)
    if n == 0:
        return "Wrong!"  # Return "Wrong!" if the list is empty
    elif n % 2 == 1:
        return fifo_list[n // 2]
    else:
        median = (fifo_list[n // 2 - 1] + fifo_list[n // 2]) / 2
        return median


def add_num(number, count_dict, fifo_list):
    count_dict[number] = count_dict.get(number, 0) + 1
    if number not in fifo_list:
        fifo_list.append(number)
        fifo_list.sort()

def remove_num(number, count_dict, fifo_list):
    print("Before removal:", fifo_list)  # Print the list before removal
    print("Removing:", number)  # Print the number we're trying to remove
    if number in fifo_list:
        fifo_list = [x for x in fifo_list if x != number]  # Remove all instances of the number from the list
        count_dict[number] -= 1  # Decrement the count of the removed number
    else:
        fifo_list.remove(number)  # Remove all instances of the number from the list
        count_dict[number] -= 1  # Decrement the count of the removed number
        print("After removal:", fifo_list)  # Print the list after removal
 

if __name__ == "__main__":
    number_operations = int(input())
    count_dict = {}
    fifo_list = []
    medians = []  # List to store all the medians
    has_valid_medians = False  # Flag to track if any valid medians are found

    # Collect all the operations
    for _ in range(number_operations):
        operation = input().split()
        op_type = operation[0]
        num = int(operation[1])

        if op_type == 'a':
            add_num(num, count_dict, fifo_list)
        elif op_type == 'r':
            remove_num(num, count_dict, fifo_list)

        # Calculate the median after each operation and store it
        medians.append(calculate_median(fifo_list))
        if medians[-1] != "Wrong!":
            has_valid_medians = True  # Update the flag if a valid median is found

    # Print the result
    for median in medians:
        if median != "Wrong!":
            print(median)

    # Print "Wrong!" if no valid medians are found
    if not has_valid_medians:
        print("Wrong!")

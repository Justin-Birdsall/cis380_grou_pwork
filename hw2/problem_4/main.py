def calculate_median(fifo_list):
    n = len(fifo_list)
    if n == 0:
        return "Wrong!"  # Return "Wrong!" if the list is empty
    elif n % 2 == 1:
        return fifo_list[n // 2]
    else:
        median = (fifo_list[n // 2 - 1] + fifo_list[n // 2]) / 2
        return median


def add_num(number, dict, fifo_list):
    dict[number] = dict.get(number, 0) + 1
    if number not in fifo_list:
        fifo_list.append(number)
        fifo_list.sort()

# def remove_num(number, dict, fifo_list):
#     if number not in dict or dict[number] == 0:
#         #print("Wrong!")
#         pass
#     else:
#         dict[number] -= 1
#         if dict[number] == 0:
#             fifo_list.remove(number)
    
def remove_num(number, count_dict, fifo_list):
    if number not in count_dict or count_dict[number] == 0:
        #print("Wrong!")
        pass
    else:
        while number in fifo_list:
            fifo_list.remove(number)
        count_dict[number] = 0


# if __name__ == "__main__":

#     number_operations= int(input())
#     #a dictionary is going to work well here
#     #it's efficient in that you can just add the numberber that is passed in and should be o(1) to see if that number exists or not
#     dict = {}
    
#    #since this is a fifo problem a list should be pretty efficent at fist glace (maybe? a more efficient data structure)= []
#     fifo_list = []
#     #
#     #now we need all of our information so loop and add
#     for _ in range(number_operations):
#         #need to split it for the char and numbers since they are space delimited
#         operation = input().split()
#         add_or_remove = operation[0]
#        #get the other half of the list where the number is  
#         number = int(operation[1])
#        #now we need to check if it is an add or remove and call the respective function
#         if add_or_remove == 'a':
#            add_num(number, dict, fifo_list)
#         elif add_or_remove == 'r':
#             remove_num(number, dict, fifo_list)
#         #now we have to calculate our median
#     calculate_median(fifo_list)
       
if __name__ == "__main__":
    number_operations = int(input())
    count_dict = {}
    fifo_list = []
    medians = []  # List to store all the medians

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

    # Check if all the medians are "Wrong!"
    all_wrong = all(median == "Wrong!" for median in medians)

    # Print the result
    for median in medians:
        if median != "Wrong!":
            print(median)

    # Print "Wrong!" only if all medians are "Wrong!"
    if all_wrong and medians:
        print("Wrong!")

           
# def peek_min_heap(heap):
#     if not heap:
#         return None
#     return int(heap[0])

# def insert_min_heap(heap, value):
#     heap.append(value)
#     index = len(heap) - 1
#     while index > 0 and heap[(index - 1) // 2] > heap[index]:
#         heap[index], heap[(index - 1) // 2] = heap[(index - 1) // 2], heap[index]
#         index = (index - 1) // 2

# def delete_min_heap(heap, value):
#     index = -1
#     for i in range(len(heap)):
#         if heap[i] == value:
#             index = i
#             break
#     if index == -1:
#         return
    
#     # Replace the value to be deleted with the last element
#     heap[index] = heap[-1]
#     heap.pop()  # Remove the last element
    
#     # Heapify to maintain the heap property
#     current_index = index
#     while True:
#         left_child = 2 * current_index + 1
#         right_child = 2 * current_index + 2
#         smallest = current_index
#         if left_child < len(heap) and heap[left_child] < heap[smallest]:
#             smallest = left_child
#         if right_child < len(heap) and heap[right_child] < heap[smallest]:
#             smallest = right_child
#         if smallest != current_index:
#             heap[current_index], heap[smallest] = heap[smallest], heap[current_index]
#             current_index = smallest
#         else:
#             break

# def overlap(overlaps, sum, messages_dict):
#     fastest_decrypt = []
#     message_table = messages_dict
#     timings = overlaps
#     new_sum = sum
#     overlap_speed = 0
#     #add all overlapping messages to a new heap
#     for i in timings:
#         overlap_speed = message_table[timings[i]]
#         insert_min_heap(fastest_decrypt, overlap_speed)
#     for i in timings:
#         speed_to_sum = peek_min_heap(fastest_decrypt)
#         if speed_to_sum is None:
#             break
#         new_sum += speed_to_sum - timings[i]
#         delete_min_heap(fastest_decrypt, speed_to_sum)
        
#     return new_sum

# # if __name__ == "__main__":
# #     number_operations = int(input())
# #     timings_dict = {}
# #     min_heap= []
# #     faster_message_lookup = {}

# #     for _ in range(number_operations):
# #         time_of_arrival, time_to_decrypt = map(int, input().split())
# #         insert_min_heap(min_heap,time_of_arrival)
# #         #faster_message_lookup[time_to_decrypt] = time_of_arrival
# #         timings_dict[time_of_arrival] = time_to_decrypt

    
   
# #     for i in range(number_operations):
# #         min = peek_min_heap(min_heap)
# #         print("the root of the heap (mins value is)", min)
# #         #fist if i == 0 for first case
# #         if i == 0:
# #             time_step = timings_dict[min]+min
# #             sum_decrypt_time = timings_dict[min]
# #             print (time_step, "time step for 0")
# #         elif i == number_operations-1:
# #             sum_decrypt_time += timings_dict[min]
# #             print("sum decrypt time")
# #         #for ever other case besides first&last one
# #         else:
# #             min = peek_min_heap(min_heap)
# #             overlapping_messages = []
# #             while min < time_step:
# #                 overlapping_messages = [min]
# #                 delete_min_heap(min_heap,min)
# #                 min = peek_min_heap(min_heap)
            
# #             overlap(min_heap, overlapping_messages, sum_decrypt_time, timings_dict)              
        
# #                 # else:
# #                 #     time_step += timings_dict[min]
# #                 #     print(time_step, "time step for middle number", min)
# #                 #     sum_decrypt_time += (time_step - min)
# #         delete_min_heap(min_heap, min)
        
        

# #     average_decrypt_time = sum_decrypt_time / number_operations
# #     print(average_decrypt_time)
# if __name__ == "__main__":
#     number_operations = int(input())
#     timings_dict = {}
#     min_heap= []
#     faster_message_lookup = {}

#     for _ in range(number_operations):
#         time_of_arrival, time_to_decrypt = map(int, input().split())
#         insert_min_heap(min_heap,time_of_arrival)
#         timings_dict[time_of_arrival] = time_to_decrypt

#     sum_decrypt_time = 0  # Initialize sum_decrypt_time outside the loop
   
#     for i in range(number_operations):
#         min = peek_min_heap(min_heap)
#         if min is None:  # Check if min is None (heap is empty)
#             break  # Exit the loop if heap is empty
#         print("the root of the heap (mins value is)", min)
#         if i == 0:
#             time_step = timings_dict[min] + min
#             sum_decrypt_time = timings_dict[min]
#             print (time_step, "time step for 0")
#         elif i == number_operations - 1:
#             sum_decrypt_time += timings_dict[min]
#             print("sum decrypt time")
#         else:
#             overlapping_messages = []
#             while min < time_step:
#                 overlapping_messages.append(min)
#                 delete_min_heap(min_heap, min)
#                 min = peek_min_heap(min_heap)
#                 if min is None:  # Check if min is None (heap is empty)
#                     break  # Exit the loop if heap is empty
            
#             overlap(overlapping_messages, sum_decrypt_time, timings_dict)
        
#         if min is not None:  # Check if min is not None before deleting
#             delete_min_heap(min_heap, min)

#     average_decrypt_time = sum_decrypt_time / number_operations
#     print(average_decrypt_time)
import heapq

def overlap(overlaps, sum, messages_dict):
    fastest_decrypt = []
    message_table = messages_dict
    timings = overlaps
    new_sum = sum
    overlap_speed = 0
    # Add all overlapping messages to a new heap
    for timing in timings:
        overlap_speed = message_table[timing]
        heapq.heappush(fastest_decrypt, overlap_speed)
    for timing in timings:
        speed_to_sum = heapq.heappop(fastest_decrypt)
        new_sum += speed_to_sum - timing
    return new_sum

if __name__ == "__main__":
    number_operations = int(input())
    timings_dict = {}
    arrival_list=  []
    for _ in range(number_operations):
        time_of_arrival, time_to_decrypt = map(int, input().split())
        arrival_list.append(time_of_arrival)
        timings_dict[time_of_arrival] = time_to_decrypt
    #push onto heap
    min_heap = heapq.heappush(arrival_list, number_operations)
    
    # Initialize
    min = heapq.heappop(min_heap)
    time_step = timings_dict[min] + min
    sum_decrypt_time = timings_dict[min]
    print (time_step, "time step for 0")
    
    
    for messages in min_heap:
        if min_heap:  # Check if min_heap is not empty
            smallest = heapq.nsmallest(1, min_heap)
        else:
            break  # Exit the loop if heap is empty
        print("the root of the heap (mins value is)", smallest)
        if(smallest < time_step):
            overlapping_messages = []
            while smallest < time_step:
                overlapping_messages.append(smallest)
                if min_heap:
                    heapq.heappop(min_heap)
                    smallest = heapq.nsmallest(1,min_heap)
                else:
                    break
            overlap(overlapping_messages, sum_decrypt_time, timings_dict)
    average_decrypt_time = sum_decrypt_time / number_operations
    print(average_decrypt_time)
 
def minHeapify(arr, i, n):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
 
    if left < n and arr[left] < arr[smallest]:
        smallest = left
 
    if right < n and arr[right] < arr[smallest]:
        smallest = right
 
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        minHeapify(arr, smallest, n)
def insert_min_heap(heap, value):
    heap.append(value)
    index = len(heap) - 1
    while index > 0 and heap[(index - 1) // 2] > heap[index]:
        heap[index], heap[(index - 1) //
                          2] = heap[(index - 1) // 2], heap[index]
        index = (index - 1) // 2
 
 
def delete_min_heap(heap, value):
    index = -1
    for i in range(len(heap)):
        if heap[i] == value:
            index = i
            break
    if index == -1:
        return
    heap[index] = heap[-1]
    heap.pop()
    while True:
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index
        if left_child < len(heap) and heap[left_child] < heap[smallest]:
            smallest = left_child
        if right_child < len(heap) and heap[right_child] < heap[smallest]:
            smallest = right_child
        if smallest != index:
            heap[index], heap[smallest] = heap[smallest], heap[index]
            index = smallest
        else:
            break
 
 

 
if __name__ == "__main__":
    arr = [10, 5, 15, 2, 20, 30]
 
    print("Original array:", arr)
 
    # Perform heapify operation on a min-heap
    for i in range(len(arr) // 2 - 1, -1, -1):
        minHeapify(arr, i, len(arr))
 
    print("Min-Heap after heapify operation:", arr)
    heap = []
    values = [13, 16, 31, 41, 51, 100]
    for value in values:
        insert_min_heap(heap, value)
    print("Initial heap:", heap) 
    delete_min_heap(heap, 13)
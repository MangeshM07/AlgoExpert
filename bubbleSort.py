# Time complexity O(n*2) | Space Complexity O(1)
# Bubble sort performs inplace sorting
def bubble_sort(input_array):
    for i in range(len(input_array)):
        for j in range(0, len(input_array)-i-1):
            if input_array[j] > input_array[j+1]:
                input_array[j], input_array[j+1] = input_array[j+1], input_array[j]

def bubbleSort_soution2(array):
    isSorted = False
    counter = 0
    while not isSorted:
        for i in range(len(array)-1-counter):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                isSorted = False
                counter += 1


my_numbers = [64, 34, 25, 12, 22, 11, 90]

print("Original array:", my_numbers)
bubble_sort(my_numbers)
print("Sorted array:", my_numbers)
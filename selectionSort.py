# Time O(n*2) | Space O(1)
def selectionSort(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[j], array[i] = array[i], array[j]

    return array


my_numbers = [64, 34, 25, 12, 22, 11, 90, 2]

print("Original array:", my_numbers)
selectionSort(my_numbers)
print("Sorted array:", my_numbers)

# Time complexity O(n*2) | Space O(1)
def insertionSort(array):
    for i in range(1, len(array)):
        j=i
        while j > 0 and array[j] < array[j-1]:
            array[j] , array[j-1] = array[j-1], array[j]
            j -= 1

my_numbers = [64, 34, 25, 12, 22, 11, 90]

print("Original array:", my_numbers)
insertionSort(my_numbers)
print("Sorted array:", my_numbers)
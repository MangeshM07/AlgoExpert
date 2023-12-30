def searchElementInBinaryTree(array, element):
    low = 0
    high = len(array)-1

    while low <= high:
        mid = (low + high)//2
        if array[mid] == element:
            return mid
        elif array[mid] > element:
            high = mid -1
        else:
            low = mid + 1
    return -1


array = [0,1,21,33,45,45,61,71,72,73]
target = 61

print(searchElementInBinaryTree(array, target))
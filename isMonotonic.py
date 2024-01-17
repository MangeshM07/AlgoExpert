def isMonotonic(array):
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(len(array)-1):
        isNonDecreasing = isNonDecreasing and array[i] <= array[i+1]
        isNonIncreasing = isNonIncreasing and array[i] >= array[i+1]

    return isNonDecreasing or isNonIncreasing


array = [-1, -100, -1000, -1100, -1100, -9000]
print(isMonotonic(array))
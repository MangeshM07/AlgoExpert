def firstDuplicateValue_solution1(array):

    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] == array[j]:
                return array[i]
    return -1

def firstDuplicateValue_solution2(array):

    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] == array[j]:
                return array[i]
    return -1

array = [3,1,5,2,3,3,4,2]
print(firstDuplicateValue_solution1(array))

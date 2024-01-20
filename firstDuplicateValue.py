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
#
# Time Complexity:
#
# The time complexity of this solution is O(N), where N is the number of elements in the array. In the worst case,
# we may need to iterate through the entire array.
#
# Space Complexity:
#
# The space complexity is O(min(N, M)), where N is the number of elements in the array, and M is the number of unique
# elements. In the worst case, when all elements are unique, the space complexity is O(N), but in typical cases with
# duplicates, it is O(M).
def firstDuplicateValue_solution3(array):
    seen = set()

    for num in array:
        if num in seen:
            return num
        seen.add(num)
    return -1


array = [3,1,5,2,3,3,4,2]
print(firstDuplicateValue_solution3(array))

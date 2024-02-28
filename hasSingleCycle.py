# O(n) time | O(1) space
def hasSingleCycle(array):
    numElementVisited = 0
    currentIdx = 0

    while numElementVisited < len(array):
        if numElementVisited > 0 and currentIdx == 0:
            return False
        numElementVisited += 1
        currentIdx = getNextIdx(currentIdx, array)
    return currentIdx == 0


def getNextIdx(currentIdx, array):
    jump = array[currentIdx]
    nextIdx = (currentIdx + jump) % len(array)
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)


arr = [2,3,1,-4,-4,2]
print(hasSingleCycle(arr))

arr1 = [1, -1, 1, -1]
print(hasSingleCycle(arr1))
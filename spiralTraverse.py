# O(N) time | O(N) space where N is the number of elements in the array
def spiralTraverse(array):
    result = []
    startRow, endRow = 0, len(array)-1
    startCol, endCol = 0, len(array[0])-1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])

        for row in range(startRow + 1, endRow+1):
            result.append(array[row][endCol])

        for col in reversed(range(startCol, endCol)):
            result.append(array[endRow][col])

        for row in reversed(range(startRow+1, endRow)):
            result.append(array[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1



    return result

array = [
  [1,  2,  3,  4],
  [10, 11, 12, 5],
  [9,  8,  7,  6],
]

print(spiralTraverse(array))
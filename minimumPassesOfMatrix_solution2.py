# O(w*h) time | O(w*h) space
def minimumPassesOfMatrix(matrix):
    passes = convertNegatives(matrix)
    return passes-1 if not containsNegatives(matrix) else -1


def convertNegatives(matrix):
    queue = getAllPositivePositions(matrix)

    passes = 0

    while len(queue) > 0:
        currentSize = len(queue)


        while currentSize > 0:
            currentRow, currentCol = queue.pop(0)

            adjacentPositions = getAdjacentPositions(currentRow, currentCol, matrix)
            for position in adjacentPositions:
                row, col = position

                value = matrix[row][col]
                if value < 0:
                    matrix[row][col] = value * -1
                    queue.append([row, col])

            currentSize -=1
        passes += 1

    return passes


def getAllPositivePositions(matrix):
    positivePositions = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            value = matrix[row][col]
            if value > 0:
                positivePositions.append([row, col])

    return positivePositions


def getAdjacentPositions(row, col, matrix):
    adjacentPositions = []

    if row > 0:
        adjacentPositions.append([row-1, col])
    if row < len(matrix)-1:
        adjacentPositions.append([row+1, col])
    if col > 0:
        adjacentPositions.append([row, col-1])
    if col < len(matrix[0])-1:
        adjacentPositions.append([row, col+1])

    return adjacentPositions


def containsNegatives(matrix):
    for row in matrix:
        for value in row:
            if value < 0:
                return True

    return False


matrix = [
  [0, -1, -3, 2, 0],
  [1, -2, -5, -1, -3],
  [3, 0, 0, -4, -1]
]

print(minimumPassesOfMatrix(matrix))

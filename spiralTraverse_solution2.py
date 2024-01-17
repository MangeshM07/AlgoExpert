# O(N) space | O(1) time
def spiralTraverse(matrix):
    result = []
    while matrix:
        # Traverse top row
        result += matrix.pop(0)

        if matrix and matrix[0]:
            # Traverse right column
            for row in matrix:
                result.append(row.pop())

        if matrix:
            # Traverse bottom row
            result += matrix.pop()[::-1]

        if matrix and matrix[0]:
            # Traverse left column
            for row in matrix[::-1]:
                result.append(row.pop(0))

    return result

array = [
  [1,  2,  3,  4],
  [10, 11, 12, 5],
  [9,  8,  7,  6],
]

result = spiralTraverse(array)
print(result)

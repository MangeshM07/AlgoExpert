# O(2^(n+m)) time | O(n+m) space
def numberOfWaysToTraverseGraph_sol1(width, height):
    if width==1 and height==1:
        return 1

    return numberOfWaysToTraverseGraph_sol1(width-1, height) + numberOfWaysToTraverseGraph_sol1(width, height-1)

# O(n*m) time | O(n*m) space
def numberOfWaysToTraverseGraph_sol2(width, height):
    numberOfWays = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

    for widthIdx in range(1, width + 1):
        for heightIdx in range(1, height + 1):
            if widthIdx == 1 or heightIdx == 1:
                numberOfWays[heightIdx][widthIdx] = 1
            else:
                waysLeft = numberOfWays[heightIdx][widthIdx-1]
                waysUp = numberOfWays[heightIdx-1][widthIdx]
                numberOfWays[heightIdx][widthIdx] = waysLeft + waysUp

    return numberOfWays[height][width]

# O(n+m) time | O(1) space
def numberOfWaysToTraverseGraph_sol3(width, height):
    xDistanceToCorner = width - 1
    yDistanceToCorner = height - 1

    numerator = factorial(xDistanceToCorner + yDistanceToCorner)
    denominator = factorial(xDistanceToCorner) * factorial(yDistanceToCorner)
    return numerator // denominator


def factorial(num):
    result = 1

    for n in range(2, num+1):
        result *= n

    return result


width = 4
height = 3

print(numberOfWaysToTraverseGraph_sol3(width, height))



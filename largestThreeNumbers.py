def largestThreeNumbers_solution1(array):
    newArr = sorted(array)
    return newArr[-3:]


def largestThreeNumbers_solution2(array):
    threeLargest = [None] * 3
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest


def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)


def shiftAndUpdate(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]


def largestThreeNumbers_solution3(array):
    if len(array) < 3:
        return "Array should have at least three elements."

    first = second = third = float('-inf')

    for num in array:
        if num > first:
            third = second
            second = first
            first = num
        elif num > second:
            third = second
            second = num
        elif num > third:
            third = num

    return [third, second, first]

# Example usage:
array = [10, 5, 2, 9, 12, 7, 17, 4]
result = largestThreeNumbers_solution3(array)
print(result)


arr = [141, 1, 17, -7, -17, -27, 18, 541, 541, 8, 7, 7]
print(largestThreeNumbers_solution3(arr))

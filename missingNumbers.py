def missingNumbers(nums):
    includedNums = set(nums)

    solution = []
    for num in range(1, len(nums) + 3):
        if num not in includedNums:
            solution.append(num)

    return solution

nums = [1,4,3]
print(missingNumbers(nums))
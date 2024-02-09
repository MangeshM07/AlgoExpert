
# O(n) time | O(1) space
def maxSubsetSumNoAdjacent(array):
    currentMax, previousMax = 0,0
    for number in array:
        previousMax, currentMax = currentMax, max(currentMax, previousMax+number)
    return currentMax


array = [75, 105, 120, 75, 90, 135]
print(maxSubsetSumNoAdjacent(array))
# Let's break this down:
#
# previousMax, currentMax = currentMax, max(currentMax, previousMax + num )
#
# This line is doing two things at once due to the simultaneous assignment in Python. The `previousMax` is updated to
# be the last `currentMax` (essentially shifting the "window" one step forward), and then we calculate the new
# `currentMax`.
#
# max(currentMax, previousMax + num) This is the key part that ensures we only look at non-adjacent numbers. We're
# deciding between two options for our new `currentMax`:
#
# - The old `currentMax` value: This represents the case where we don't take the current number (i.e., we "skip" it).
# Thus the maximum sum up to this point stays the same. This is how we can ignore adjacent values because we always
# have the option to just keep our old `currentMax` and skip the current number.
#
# - The `previousMax + num`: This represents the case where we take the current number. But we can't add it to
# `currentMax` because that would mean we're using two adjacent numbers. So we add it to `previousMax` instead.
#
# Hence, at each step, the algorithm always makes sure that it never includes two adjacent numbers in the sum. By
# choosing the maximum of the above two options, we ensure we're always keeping the maximum sum of non-adjacent
# numbers up to the current position in the array.
#
# The algorithm eventually returns the `currentMax`, which after going through all the numbers in the array,
# represents the maximum sum of non-adjacent numbers in the entire array.
#

# Upper Bound: O(n^2 * n!) time | O(n*n!) space
# Roughly: O(n * n!) time | O(n*n!) space
def getPermutations(array):
    permutations = []
    permutationsHelper(array, [], permutations)
    return permutations


def permutationsHelper(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i+1:] #O(n)
            newPermutation = currentPermutation + [array[i]] #O(n)
            permutationsHelper(newArray, newPermutation, permutations)


a = [1,2,3]
print(getPermutations(a))
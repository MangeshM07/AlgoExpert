def getPermutations(array):

    def helper(array):
        if len(array) == 1:
            yield array

        for idx, element in enumerate(array):
            a = array[:idx]
            b = array[idx+1:]
            remaining = a + b
            # remaining = array[:idx] + array[idx+1:]
            for sub_perm in helper(remaining):
                yield [element] + sub_perm

    return list(helper(array))


a = [1,2,3]
print(getPermutations(a))
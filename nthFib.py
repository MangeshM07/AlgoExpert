def getNthFib(n):
    a , b = 0 ,1

    for _ in range(n-1):
        a, b = b, a+b

    return a

# time complexity O(2^n) | Space O(n) since function call stack is used
def getNthfib_solution2(n):
    if n==2:
        return 1
    elif n==1:
        return 0
    else:
        return getNthfib_solution2(n-1) + getNthfib_solution2(n-2)

# O(n) space and time
def getNthfib_solution3(n, memoize = {1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthfib_solution3(n - 1, memoize) + getNthfib_solution3(n-2, memoize)
        return memoize[n]


num = getNthfib_solution3(5)
print(num)
# O(nd) time | O(n) space
def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for amount in range(n+1)]
    ways[0] = 1

    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] += ways[amount-denom]
    return ways[n]

def numberOfWaysToMakeChange_optimized(n, denoms):
    # Write your code here.
    waysToMakeChange = [1] + [0 for _ in range(n)]
    for denom in denoms:
        for change in range(denom, n+1):
            waysToMakeChange[change] += waysToMakeChange[change-denom]
    return waysToMakeChange[-1]

n = 10
denoms = [1,5,10,25]
print(numberOfWaysToMakeChange(n, denoms))

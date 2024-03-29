# O(nd) time | O(n) space
def minNumberOfCoinsForChange(n ,denoms):
    numOfCoins = [float("inf") for amount in range(n+1)]
    numOfCoins[0] = 0
    for denom in denoms:
        for amount in range(len(numOfCoins)):
            if denom <= amount:
                numOfCoins[amount] = min(numOfCoins[amount], 1+numOfCoins[amount-denom])
    return numOfCoins[n] if numOfCoins[n] != float("inf") else -1


n=6
denoms = [1,2,5,10]
print(minNumberOfCoinsForChange(n, denoms))
# O(n log(n)) time | O(n) space

def sweetAndSavoury(dishes, target):
    sweetDishes = sorted([dish for dish in dishes if dish < 0], key=abs)
    savouryDishes = sorted([dish for dish in dishes if dish > 0])

    bestPair = [0,0]
    bestDifference = float('inf')
    sweetIndex, savouryIndex = 0,0

    while sweetIndex < len(sweetDishes) and savouryIndex < len(savouryDishes):
        currentSum = sweetDishes[sweetIndex] + savouryDishes[savouryIndex]

        if currentSum <= target:
            currentDifference = target - currentSum
            if currentDifference < bestDifference:
                bestDifference = currentDifference
                bestPair = [sweetDishes[sweetIndex], savouryDishes[savouryIndex]]
            savouryIndex += 1
        else:
            sweetIndex += 1
    return bestPair


dishes = [2, 5, -4, -7, 12, 100, -25]
target =  -7

print(sweetAndSavoury(dishes, target))
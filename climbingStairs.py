def climbingStairs(noOfSteps):
    if noOfSteps == 1:
        return 1
    elif noOfSteps == 2:
        return 2
    else:
        return climbingStairs(noOfSteps - 2) + climbingStairs(noOfSteps - 1)


noOfSteps = 8
print(climbingStairs(noOfSteps))




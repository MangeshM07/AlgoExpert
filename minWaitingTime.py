# Time O(n log n) | space O(1) time

def minWaitingTime(queries):
    queries.sort()

    totalWaitingTime = 0

    for idx, duration in enumerate(queries):
        queriesLeft = len(queries) - (idx + 1)
        totalWaitingTime += duration * queriesLeft

    return totalWaitingTime

q = [3,2,1,2,6]
print(minWaitingTime(q))
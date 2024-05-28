# O(n+m) time | O(n) space
def mergingLinkedLists(linkedListOne, linkedListTwo):
    listOneNodes = set()
    currentNodeOne = linkedListOne
    while currentNodeOne is not None:
        listOneNodes.add(currentNodeOne)
        currentNodeOne = currentNodeOne.next

    currentNodeTwo = linkedListTwo
    while currentNodeTwo is not None:
        if currentNodeTwo in listOneNodes:
            return currentNodeTwo
        currentNodeTwo = currentNodeTwo.next
    return None

# O(n+m) time | O(1) space
def mergingLinkedLists_sol2(linkedListOne, linkedListTwo):
    currentNodeOne = linkedListOne
    countOne = 0
    while currentNodeOne is not None:
        countOne += 1
        currentNodeOne = currentNodeOne.next

    currentNodeTwo = linkedListTwo
    countTwo = 0
    while currentNodeTwo is not None:
        countTwo += 1
        currentNodeTwo = currentNodeTwo.next

    difference = abs(countTwo - countOne)
    biggerCurrentNode = linkedListOne if countOne > countTwo else linkedListTwo
    smallerCurrentNode = linkedListTwo if countTwo > countOne else linkedListOne

    for _ in range(difference):
        biggerCurrentNode = biggerCurrentNode.next

    while biggerCurrentNode is not smallerCurrentNode:
        biggerCurrentNode = biggerCurrentNode.next
        smallerCurrentNode = smallerCurrentNode.next

    return biggerCurrentNode
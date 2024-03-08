# O(v+e) time | O(v) space


WHITE, GREY, BLACK = 0, 1, 2
# WHITE means unvisited
# GREY means visited but not fully processed, still in recursive stack
# BLACK fully processed


def cycleInGraph(edges):
    numberOfNodes = len(edges)
    colors = [WHITE for _ in range(numberOfNodes)]

    for node in range(numberOfNodes):
        if colors[node] != WHITE:
            continue

        containsCycle = traverseAndColorNodes(node, edges, colors)
        if  containsCycle:
            return True

    return False


def traverseAndColorNodes(node, edges, colors):
    colors[node] = GREY

    neighbors = edges[node]
    for neighbor in neighbors:
        neighborColor = colors[neighbor]

        if neighborColor == GREY:
            return True

        if neighborColor != WHITE:
            continue

        containsCycle = traverseAndColorNodes(neighbor, edges, colors)
        if containsCycle:
            return True

    colors[node] = BLACK
    return False

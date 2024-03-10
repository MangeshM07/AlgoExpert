
# O(v+e) time | O(v) space
def twoColorable(edges):
    colors = [None for _ in edges]
    colors[0] = True
    stack = [0]

    while len(stack) > 0:
        node = stack.pop()
        for connection in edges[node]:
            if colors[connection] is None:
                colors[connection] = not colors[node]
                stack.append(connection)
            elif colors[connection] == colors[node]:
                return False

    return True


edges= [[1],[0]]
print(twoColorable(edges))
# Time O(n) | Space O(h)

def evaluateExpressionTree(tree):
    if tree.value >= 0:
        return tree.value

    leftValue = evaluateExpressionTree(tree.left)
    rightValue = evaluateExpressionTree(tree.right)

    if tree.value == -1:
        return leftValue + rightValue
    elif tree.value == -2:
        return leftValue - rightValue
    elif tree.value == -3:
        return int(leftValue / rightValue)
    elif tree.value == -4:
        return leftValue * rightValue

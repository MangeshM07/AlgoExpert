
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    global longestPath
    longestPath = 0
    calculateLongestPath(tree)
    return longestPath


def calculateLongestPath(tree):
    global longestPath
    if tree is None:
        return 0
    leftDepth = calculateLongestPath(tree.left)
    rightDepth = calculateLongestPath(tree.right)

    curr_longestPath = leftDepth + rightDepth
    longestPath = max(curr_longestPath, longestPath)

    return max(leftDepth, rightDepth)+1

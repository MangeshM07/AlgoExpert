class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height


# O(n) time | O(h) space
def heightBalancedBinaryTree(tree):
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced


def getTreeInfo(node):
    if node is None:
        return TreeInfo(True, -1)

    leftSubTreeInfo = getTreeInfo(node.left)
    rightSubTreeInfo = getTreeInfo(node.right)

    isBalanced = (
        leftSubTreeInfo.isBalanced and rightSubTreeInfo.isBalanced
        and abs(leftSubTreeInfo.height - rightSubTreeInfo.height) <= 1
    )

    height = max(leftSubTreeInfo.height, rightSubTreeInfo.height) + 1
    return TreeInfo(isBalanced, height)
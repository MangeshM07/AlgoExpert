
# O(n) time | O(d) space - depth of tree
def invertBinaryTree_recursive(tree):
    if tree is None:
        return None
    else:
        invertBinaryTree_recursive(tree.left)
        invertBinaryTree_recursive(tree.right)
        tree.left, tree.right = tree.right, tree.left


# Iterative O(n) time | O(n) space
def invertBinaryTree_iterative(tree):
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        swapLeftAndRight(current)
        queue.append(current.left)
        queue.append(current.right)


def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

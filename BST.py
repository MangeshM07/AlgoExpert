#  Iterative approach

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average : O(log n) time | O(1) space
    # Worst : O(n) time | O(1) space
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    # Average : O(log n) time | O(1) space
    # Worst : O(n) time | O(1) space
    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
               currentNode = currentNode.left
            elif:
                currentNode = currentNode.right
            else:
                return True
        return False

    def delete(self, value):

# O(n) time | O(d) space
from bstTraversal import *
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def validateBST(self,tree):
        return self.validateBstHelper(tree, float("-inf"), float("inf"))

    def validateBstHelper(self, tree, minValue, maxValue):
        if tree is None:
            return True
        if tree.value < minValue or tree.value >= maxValue:
            return False
        leftIsValid = self.validateBstHelper(tree.right, tree.value, maxValue)
        return leftIsValid and self.validateBstHelper(tree.right, tree.value, maxValue)


tree= {
"nodes": [
  {"id": "10", "left": "5", "right": "15", "value": 10},
  {"id": "15", "left": "13", "right": "22", "value": 15},
  {"id": "22", "left": None, "right": None, "value": 22},
  {"id": "13", "left": None, "right": "14", "value": 13},
  {"id": "14", "left": None, "right": None, "value": 14},
  {"id": "5", "left": "2", "right": "5-2", "value": 5},
  {"id": "5-2", "left": None, "right": None, "value": 5},
  {"id": "2", "left": "1", "right": None, "value": 2},
  {"id": "1", "left": None, "right": None, "value": 1}
],
"root": "10"
}

# Function to build tree from JSON representation
def buildTree(tree_data):
    node_map = {}
    for node_data in tree_data["nodes"]:
        node_map[node_data["id"]] = BST(node_data["value"])
    for node_data in tree_data["nodes"]:
        node = node_map[node_data["id"]]
        if node_data["left"]:
            node.left = node_map[node_data["left"]]
        if node_data["right"]:
            node.right = node_map[node_data["right"]]
    return node_map[tree_data["root"]]

# Create BST instance
bst = BST(None)

# Build the tree from the given structure
root = buildTree(tree)

# Validate the BST
result = bst.validateBST(root)
print("Is BST:", result)

print("In Order Traversal of BST : ", inOrderTraverse(root, array=[]))
print("In Order Traversal of BST : ", preOrderTraverse(root, array=[]))
print("In Order Traversal of BST : ", postOrderTraverse(root, array=[]))

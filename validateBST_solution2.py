class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # O(n) space | O(d) space
    def validateBST(self, tree, leftParent=None, rightParent=None):
        if tree is None:
            return True
        elif leftParent is not None and tree.value >= leftParent.value:
            return False
        elif rightParent is not None and tree.value < rightParent.value:
            return False
        return self.validateBST(tree.left, tree, rightParent) and self.validateBST(tree.right, leftParent, tree)


tree = {
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

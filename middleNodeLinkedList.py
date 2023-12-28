# O(n) time | O(1) space
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def middleNode(self, linkedlist):
        slowNode = linkedlist
        fastNode = linkedlist

        while fastNode is not None and fastNode.next is not None:
            slowNode = slowNode.next
            fastNode = fastNode.next.next

        return slowNode


# Example usage:
def create_linked_list(nodes):
    head = LinkedList(nodes[0]["value"])
    current = head

    for node_data in nodes[1:]:
        current.next = LinkedList(node_data["value"])
        current = current.next

    return head

def print_linked_list(linkedlist):
    result = []
    current = linkedlist
    while current is not None:
        result.append(current.value)
        current = current.next
    print(result)

# Creating the linked list
nodes_data = [
    {"id": "1", "next": "1-2", "value": 1},
    {"id": "1-2", "next": "1-3", "value": 1},
    {"id": "1-3", "next": "2", "value": 1},
    {"id": "2", "next": "3", "value": 3},
    {"id": "3", "next": "3-2", "value": 4},
    {"id": "3-2", "next": "3-3", "value": 4},
    {"id": "3-3", "next": "4", "value": 4},
    {"id": "4", "next": "5", "value": 5},
    {"id": "5", "next": "5-2", "value": 6},
    {"id": "5-2", "next": None, "value": 6}
]

linked_list = create_linked_list(nodes_data)

# Printing the original linked list
print("Original Linked List:")
print_linked_list(linked_list)

# Finding middle node
middle_node = linked_list.middleNode(linked_list)
print("Middle Node Value:", middle_node.value)

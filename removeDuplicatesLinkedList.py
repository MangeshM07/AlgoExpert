class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    # O(n) time | O(1) space
    def removeDuplicatesFromLinkedList(self, linkedlist):
        currentNode = linkedlist

        while currentNode is not None:
            nextDistinctNode = currentNode.next
            while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
                nextDistinctNode = nextDistinctNode.next

            currentNode.next = nextDistinctNode
            currentNode = currentNode.next

        return linkedlist

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

# Removing duplicates
linked_list.removeDuplicatesFromLinkedList(linked_list)

# Printing the linked list after removing duplicates
print("Linked List after Removing Duplicates:")
print_linked_list(linked_list)

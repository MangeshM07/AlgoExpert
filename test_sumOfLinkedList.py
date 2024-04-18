import sumOfLinkedLists
import unittest


class LinkedList(sumOfLinkedLists.LinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self


def getNodesInArray(output):
    nodes = []
    current = output
    while current is not None:
        nodes.append(current.value)
        current = current.next
    return nodes

class TestsumOfLinkedLists(unittest.TestCase):
    def test_case_1(self):
        ll1 = LinkedList(2).addMany([4, 7, 1])
        ll2 = LinkedList(9).addMany([4, 5])
        expected = LinkedList(1).addMany([9, 2, 2])
        actual = sumOfLinkedLists.sumOfLinkedLists(ll1, ll2)
        self.assertEqual(getNodesInArray(actual), getNodesInArray(expected))
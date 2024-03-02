# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(descendantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)
    if depthOne > depthTwo:
        return backTrackAncestralTree(descendantOne, descendantTwo, depthOne-depthTwo)
    else:
        return backTrackAncestralTree(descendantTwo, descendantOne, depthTwo-depthOne)


def getDescendantDepth(descendant, topAncestor):
    depth = 0
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor
    return depth


def backTrackAncestralTree(lowerDescendant, higherDescendant, diff):
    while diff > 0:
        lowerDescendant = lowerDescendant.ancestor
        diff -= 1
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerDescendant


# {
#   "nodes": [
#     {"ancestor": null, "id": "A", "name": "A"},
#     {"ancestor": "A", "id": "B", "name": "B"},
#     {"ancestor": "A", "id": "C", "name": "C"},
#     {"ancestor": "B", "id": "D", "name": "D"},
#     {"ancestor": "B", "id": "E", "name": "E"},
#     {"ancestor": "C", "id": "F", "name": "F"},
#     {"ancestor": "C", "id": "G", "name": "G"},
#     {"ancestor": "D", "id": "H", "name": "H"},
#     {"ancestor": "D", "id": "I", "name": "I"}
#   ]
# }

# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!
#
# import program
# import unittest
#
#
# class AncestralTree(program.AncestralTree):
#     def addDescendants(self, *descendants):
#         for descendant in descendants:
#             descendant.ancestor = self
#
#
# def new_trees():
#     ancestralTrees = {}
#     for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
#         ancestralTrees[letter] = AncestralTree(letter)
#     return ancestralTrees
#
#
# class TestProgram(unittest.TestCase):
#     def test_case_1(self):
#         trees = new_trees()
#         trees["A"].addDescendants(trees["B"], trees["C"])
#         trees["B"].addDescendants(trees["D"], trees["E"])
#         trees["D"].addDescendants(trees["H"], trees["I"])
#         trees["C"].addDescendants(trees["F"], trees["G"])
#
#         yca = program.getYoungestCommonAncestor(trees["A"], trees["E"], trees["I"])
#         self.assertTrue(yca == trees["B"])

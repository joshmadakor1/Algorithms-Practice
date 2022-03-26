'''
    Find Kth Largest Value in BST:
    Given a binary search tree, return the Kth largest value

    Time: O(N), where N is the number of nodes in the tree
    Space: O(N), where N is the number of nodes in the tree

    Last Practiced: 2022-03-26 07:58:48
'''
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    inOrderTraversalValues = []
    search(tree, inOrderTraversalValues)
    return inOrderTraversalValues[len(inOrderTraversalValues) - k]

def search(tree, array):
    if tree is None:
        return
    search(tree.left, array)
    array.append(tree.value)
    search(tree.right, array)

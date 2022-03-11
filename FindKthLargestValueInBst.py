'''
	Find Kth Largest Value in BST:
    Given a binary search tree, return the Kth largest value

    Time: O(N), where N is the number of nodes in the tree
    Space: O(N), where N is the number of nodes in the tree

    Last Practiced: 2022-03-11 11:38:12
'''
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    bstNodeValuesInOrder = []
    inOrderTraversal(tree, bstNodeValuesInOrder)
    return bstNodeValuesInOrder[len(bstNodeValuesInOrder) - k]

def inOrderTraversal(tree, bstNodeValuesInOrder):
    if tree is None:
        return
    inOrderTraversal(tree.left, bstNodeValuesInOrder)
    bstNodeValuesInOrder.append(tree.value)
    inOrderTraversal(tree.right, bstNodeValuesInOrder)
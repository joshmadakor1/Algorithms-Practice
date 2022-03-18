'''
    Node Depths:

    Given an binary tree as an input, sum up the depths of all the nodes and return
    the depth as an integer. Assume the root of the tree has a depth of 0.

    Time:  O(N), where N is the number of nodes in the tree
    Space: O(D) -> O(N), where D is the depth of the binary tree

    LastPracticed: 2022-03-18 07:01:58
'''
def nodeDepths(root, depth = 0):
    if root is None: return 0
    leftDepth = nodeDepths(root.left, depth + 1)
    rightDepth = nodeDepths(root.right, depth + 1)
    return depth + leftDepth + rightDepth


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

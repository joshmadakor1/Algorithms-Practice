'''
    Reconstruct BST (Preorder Array):
    Given an input array ordered in preorder, reconstruct a binary tree

    Time:  O(N)
    Space: O(N), where N is the length of the input array

    Last PracticedL 2022-03-21 07:29:24
'''
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    if len(preOrderTraversalValues) == 0:
        return None
    
    currentValue = preOrderTraversalValues[0]
    rightIndex = len(preOrderTraversalValues)
    
    for i in range(1, len(preOrderTraversalValues)):
        if preOrderTraversalValues[i] >= currentValue:
            rightIndex = i
            break
    
    leftBranch = reconstructBst(preOrderTraversalValues[1:rightIndex])
    rightBranch = reconstructBst(preOrderTraversalValues[rightIndex:])
    
    return BST(currentValue, leftBranch, rightBranch)
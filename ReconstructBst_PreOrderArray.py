'''
	Reconstruct BST (Preorder Array):
    Given an input array ordered in preorder, reconstruct a binary tree

    Time:  O(N)
    Space: O(N), where N is the length of the input array
'''
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    if len(preOrderTraversalValues) == 0:
        return
    
    currentValue = preOrderTraversalValues[0]
    rightIndex = len(preOrderTraversalValues)
    
    for index in range(1, len(preOrderTraversalValues)):
        if preOrderTraversalValues[index] >= currentValue:
            rightIndex = index
            break
    
    leftBranch = reconstructBst(preOrderTraversalValues[1:rightIndex])
    rightBranch = reconstructBst(preOrderTraversalValues[rightIndex:])
    
    return BST(currentValue, leftBranch, rightBranch)

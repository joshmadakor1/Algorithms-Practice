'''
	Validate BST:
    Given a binary search tree, ensure that the tree is valid
    and meets the requirements for a BST
    left child -> less than
    right child -> greater than or equal to

    Time: O(N), where N is the number of nodes in the tree
    Space: O(H), where H is the height of the recursive call stack

    Last Practiced: 2022-03-12 07:04:38
'''
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree, minValue=float("-inf"), maxValue=float("inf")):
	if tree is None: return True
	if tree.value >= minValue and tree.value < maxValue:
		leftIsValid = validateBst(tree.left, minValue, tree.value)
		rightIsValid = validateBst(tree.right, tree.value, maxValue)
		return leftIsValid and rightIsValid
	return False
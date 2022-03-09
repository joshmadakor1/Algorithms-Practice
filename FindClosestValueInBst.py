'''
    Find Closest Value In BST:
    Given a BST as an input and a target value, return the
    value of the node that is closest to the target value within
    the BST

    Best Time:  O(log(N)), where N = number of nodes in tree
    Best Space: O(log(N)), where N = depth of recursive call stack
    Worst Time/Space: O(N)/O(N), where no nodes have 2 children

    Last Practice: 2022-03-09 08:40:34
'''
def findClosestValueInBst(tree, target):
    return findClosest(tree, target, float("inf"))

def findClosest(node, target, closest):
	if node is None:
		return closest
	if abs(target - node.value) < abs(target - closest):
		closest = node.value
	if target < node.value:
		return findClosest(node.left, target, closest)
	elif target > node.value:
		return findClosest(node.right, target, closest)
	return closest
	
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

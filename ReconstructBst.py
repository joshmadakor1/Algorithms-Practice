'''
    Reconstruct BST:
    Reconstruct a binary search tree given an array that represents a
    pre-order traversal of a BST

    Time: O(N), where N is the number of elements in the array
    Space: O(N), where N isi the numbef of elements in the array (unbalanced BST) 

    Last Practice: 2022-03-13 07:36:36
'''
class BST:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right
	
def reconstructBst(array):
	if not len(array): return None
	currentValue = array[0]
	rightIndex = len(array)
	for i in range(1,len(array)):
		if array[i] >= currentValue:
			rightIndex = i
			break
	leftBranch = reconstructBst(array[1:rightIndex])
	rightBranch = reconstructBst(array[rightIndex:])
	return BST(currentValue, leftBranch, rightBranch)
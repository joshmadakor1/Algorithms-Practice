'''
    Min Height BST:
    Wrute a function that takes in a sorted array and builds a binary search 
    tree. The function should MINIMIZE the height of the BST

    Time:  O(N), where N is the length of the input array
    Space: O(N), where N is the number of nodes in the BST

    Last Practice: 2022-03-11 10:25:59
'''
def minHeightBst(array):
	mid = (len(array) - 1) // 2
	tree = BST(array[mid])
	buildMinHeightBst(array, tree, 0, mid - 1)
	buildMinHeightBst(array, tree, mid + 1, len(array) - 1)
	return tree

def buildMinHeightBst(array, tree, left, right):
	if left > right: return
	mid = (left + right) // 2
	tree.insert(array[mid])
	buildMinHeightBst(array, tree, left, mid - 1)
	buildMinHeightBst(array, tree, mid + 1, right)

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
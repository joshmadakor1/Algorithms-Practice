
'''
    Binary Tree Diameter:
    Given a binary tree, output the diameter (length of its longest path,
    regardless of if the path passes through the root)

    Time:  O(N)
    Space: O(N), (Alternate O(D), where D is the depth of binary tree)

	Last Practiced: 2022-03-23 07:19:27
'''
# This is an input class. Do not edit.
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
	def __init__(self, diameter, height):
		self.diameter = diameter
		self.height = height
		
def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter

def getTreeInfo(tree):
	if tree is None:
		return TreeInfo(0,0)
	leftTreeInfo = getTreeInfo(tree.left)
	rightTreeInfo = getTreeInfo(tree.right)
	
	maxPathOverRoot = leftTreeInfo.height + rightTreeInfo.height
	maxDiameterSoFar = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
	currentDiameter = max(maxPathOverRoot, maxDiameterSoFar)
	currentHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)
	
	return TreeInfo(currentDiameter, currentHeight)


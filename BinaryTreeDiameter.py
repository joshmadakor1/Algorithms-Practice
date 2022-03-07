
'''
	Binary Tree Diameter:
    Given a binary tree, output the diameter (length of its longest path,
    regardless of if the path passes through the root)

    Time:  O(N)
    Space: O(N), (Alternate O(D), where D is the depth of binary tree)
'''
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Helper class to keep track of the Diameter and Height of all the nodes
class TreeInfo:
	def __init__(self, diameter, height):
		self.diameter = diameter
		self.height = height

def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter

def getTreeInfo(tree):
	if tree is None:
		return TreeInfo(0,0)
	
	leftBranchInfo = getTreeInfo(tree.left)
	rightBranchInfo = getTreeInfo(tree.right)
	
	pathLengthThroughRoot = leftBranchInfo.height + rightBranchInfo.height
	totalDiameterSoFar = max(leftBranchInfo.diameter, rightBranchInfo.diameter)
	currentDiameter = max(pathLengthThroughRoot,totalDiameterSoFar)
	currentHeight = 1 + max(leftBranchInfo.height, rightBranchInfo.height)
	
	return TreeInfo(currentDiameter, currentHeight)

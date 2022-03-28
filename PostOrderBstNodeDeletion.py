'''
    Post Order BST Node Deletion
    Delete all nodes from a BST in O(N) time and print out nodes that were deleted

    Time: O(N)
    Space: O(D), where D is the depth of the BST

    Last Practiced: 2022-03-28 08:18:13
'''

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right == None:
                self.right = BST(value)
            else:
                self.right.insert(value)

def deleteNodesAndReturnOrder(node, array):
    if node.left is not None:
        deleteNodesAndReturnOrder(node.left, array)
    if node.right is not None:
        deleteNodesAndReturnOrder(node.right, array)

    array.append(node.value)
    node = None

root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)

deletedNodes = []
deleteNodesAndReturnOrder(root, deletedNodes)
print(deletedNodes)
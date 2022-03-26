'''
    BST Traversal:
    Write three functions to traverse a binary tree by:
    In-order, pre-oder, and post-order. Append each node value
    to an array and have the function return the array

    Time:  O(N), where N is the number of nodes in the tree
    Space: O(N), where N is the number of nodes in the tree

    Last Practice: 2022-03-26 08:03:14
'''
def inOrderTraverse(tree, array):
    if tree is None: return
    inOrderTraverse(tree.left, array)
    array.append(tree.value)
    inOrderTraverse(tree.right, array)
    return array

def preOrderTraverse(tree, array):
    if tree is None: return
    array.append(tree.value)
    preOrderTraverse(tree.left, array)
    preOrderTraverse(tree.right, array)
    return array

def postOrderTraverse(tree, array):
    if tree is None: return
    postOrderTraverse(tree.left, array)
    postOrderTraverse(tree.right, array)
    array.append(tree.value)
    return array
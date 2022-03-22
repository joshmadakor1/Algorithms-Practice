'''
    Breadth First Search:
    Given a tree as an input, perform a BFS traversal, adding
    each nodes value along the way to an array. Return the array.

    Time: O(V+E)
    Space: O(V)

    Last Practiced: 2022-03-22 06:24:41
'''
# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = []
        queue.append(self)
        
        while len(queue):
            currentNode = queue.pop(0)
            array.append(currentNode.name)
            for child in currentNode.children:
                queue.append(child)
        
        return array
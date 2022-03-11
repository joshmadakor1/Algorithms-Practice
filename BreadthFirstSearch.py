'''
	Breadth First Search:
    Given a tree as an input, perform a BFS traversal, adding
    each nodes value along the way to an array. Return the array.

    Time: O(V+E)
    Space: O(V)

    Last Practiced: 2022-03-11 11:29:45
'''
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        q = []
        q.append(self)
        
        while len(q):
            currentNode = q.pop(0)
            array.append(currentNode.name)
            for child in currentNode.children:
                q.append(child)
                
        return array

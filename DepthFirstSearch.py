'''
    Depth First Search:
    Perform DFS on an tree (input). Append all the nodes' values
    to an array and return the array

    Time:  O(V+E), where V=verticies and E=edges
    Space: O(V) / O(N) where V=verticies

    Last Practice: 2022-03-09 07:28:53
'''
class Node:
	def __init__(self, name):
		self.name = name
		self.children = []
		
	def addChild(self, name):
		self.children.append(Node(name))
		
	def depthFirstSearch(self, array):
		array.append(self.name)
		for child in self.children:
			child.depthFirstSearch(array)
		return array
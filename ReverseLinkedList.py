'''
    Reverse Linked List:
    Given a linked list, reverse it and return the new head node

    Time:  O(N), where N are the number of nodes in the list
    Space: O(3) -> O(1), three pointers are used for reversal operations

    Last Practice: 2022-03-18 06:54:07
'''
class LinkedList:
	def __init__(self, value):
		self.value = value
		self.next = None

def reverseLinkedList(linkedList):
	previousNode = None
	currentNode = linkedList
	while currentNode is not None:
		nextNode = currentNode.next
		currentNode.next = previousNode
		previousNode = currentNode
		currentNode = nextNode
	return previousNode
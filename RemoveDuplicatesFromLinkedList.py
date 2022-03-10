'''
	Remove Duplicates From LinkedList:
    Given a linkedlist as an input, remove the duplicates
    and return the linkedlist

    Time:  O(N)
    Space: O(1)

	Last Practiced: 2022-03-10 07:43:27
'''
class LinkedList:
	def __init__(self, value):
		self.value = value
		self.next = None
		
def removeDuplicatesFromLinkedList(linkedList):
	currentNode = linkedList
	
	while currentNode is not None:
		nextNode = currentNode.next
		while nextNode is not None and nextNode.value == currentNode.value:
			nextNode = nextNode.next
		currentNode.next = nextNode
		currentNode = nextNode
	
	return linkedList
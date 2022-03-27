'''
    Sum Of LinkedLists (https://www.algoexpert.io/questions/Sum%20of%20Linked%20Lists)

    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains a single digit.
    Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Time: O(N+M) -> O(N), where N and M are the lengths of the two input LinkedLists
    Space: O(N), where N is the number of nodes in the anwer LinkedList

    Last Practiced: 2022-03-26 08:29:14 
'''
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def sumOfLinkedLists(linkedListOne, linkedListTwo):
	number1 = []
	number2 = []
	number3 = 0
	answer = None
	
	currentNode = linkedListOne
	while currentNode is not None:
		number1.insert(0, str(currentNode.value))
		currentNode = currentNode.next
	number1 = "".join(number1)
	print(number1)
	
	currentNode = linkedListTwo
	while currentNode is not None:
		number2.insert(0, str(currentNode.value))
		currentNode = currentNode.next
	number2 = "".join(number2)	
	number3 = int(number1) + int(number2)
	number3 = str(number3)
	
	for i in reversed(range(len(number3))):
		if answer is None:
			answer = LinkedList(int(number3[i]))
			currentNode = answer
		else:
			currentNode.next = LinkedList(int(number3[i]))
			currentNode = currentNode.next
	return answer
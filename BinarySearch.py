'''
    Binary Search:
    Given a sorted array and target value as input, perform a binary
    search to find the index of the target value. Return the index

    Time:  O(log(N)), where N = number of nodes in array
    Space: O(1)
    
    Last Practice: 2022-03-09 08:45:54
'''
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
	if left > right:
		return -1
	mid = (left + right ) // 2
	if target < array[mid]:
		return binarySearchHelper(array, target, left, mid -1 )
	elif target > array[mid]:
		return binarySearchHelper(array, target, mid + 1, right)
	return mid
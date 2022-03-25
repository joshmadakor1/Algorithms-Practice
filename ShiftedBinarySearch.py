'''
    Shifted Binary Search:
    Given a sorted, shifted array of distinct elements and a target as input,
    retun the index of the target number if it exists, if not, return -1

    Time: O(logN)
    Space: O(1)

    Last Practiced: 2022-03-25 10:06:15
'''
def shiftedBinarySearch(array, target):
    return search(array, target, 0, len(array)-1)

def search(array, target, left, right):
	if left > right: return -1
	mid = (left + right) // 2
	
	# If mid index is the target, return mid
	if array[mid] == target:
		return mid
	
	# Left is sorted
	if (array[left] <= array[mid]):
		
		# Target is in left sub array
		if target >= array[left] and target < array[mid]:
			return search(array, target, left, mid - 1)
		
		# Target is in right sub array
		else:
			return search(array, target, mid + 1, right)
	
	# Right is sorted
	elif (array[mid] <= array[right]):
		
		# Target is in the right sub array
		if target > array[mid] and target <= array[right]:
			return search(array, target, mid + 1, right)
		
		# Target is in the left sub array
		else:
			return search(array, target, left, mid - 1)
		
'''
    Shifted Binary Search:
    Given a sorted, shifted array of distinct elements and a target as input,
    retun the index of the target number if it exists, if not, return -1

    Time: O(N)
    Space: O(1)

    Last Practiced: 2022-03-22 06:04:26
'''
def shiftedBinarySearch(array, target):
	return search(array, target, 0, len(array) -1)

def search(array, target, left, right):
	if left > right: return -1
	mid = (left+right)//2
	if array[mid] == target: return mid

	# If the left side is sorted
	if array[left] <= array[mid]:
		# If the target is in the left side:
		if target < array[mid] and target >= array[left]:
			return search(array, target, 0, mid - 1)
		# If the target is in the right side:
		else:
			return search(array, target, mid + 1, right)
	# If the right side is sorted
	else:
		# If the target is in the right side:
		if target > array[mid] and target <= array[right]:
			return search(array, target, mid + 1, right)
		# If the target is in the left side:
		else:
			return search(array, target, left, mid - 1)
	
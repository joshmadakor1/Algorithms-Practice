'''
    Shifted Binary Search:
    Given a sorted, shifted array of distinct elements and a target as input,
    retun the index of the target number if it exists, if not, return -1

    Time: O(N)
    Space: O(1)

    Last Practiced: 2022-03-23 06:39:13
'''
def shiftedBinarySearch(array, target):
    return search(array, target, 0, len(array) - 1)

def search(array, target, left, right):
	if left > right: return -1
	mid = (left+right)//2
	if array[mid] == target: return mid

	# Left side is sorted
	if array[left] <= array[mid]:
		if target >= array[left] and target < array[mid]:
			return search(array, target, left, mid - 1)
		else:
			return search(array, target, mid + 1, right)
	# Right side is sorted
	elif array[mid] <= array[right]:
		if target > array[mid] and target <= array[right]:
			return search(array, target, mid + 1, right)
		else:
			return search(array, target, left, mid - 1)
	

	
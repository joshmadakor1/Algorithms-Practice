'''
    Shifted Binary Search:
    Given a sorted, shifted array of distinct elements and a target as input,
    retun the index of the target number if it exists, if not, return -1

    Time: O(N)
    Space: O(1)

    Last Practiced: 2022-03-21 05:42:20
'''
def shiftedBinarySearch(array, target):
    return search(array, 0, len(array)-1, target)


def search(array, left, right, target):
	if left > right: return -1
	mid = (left+right)//2
	if array[mid] == target: return mid
	
	# Left is in order
	if array[left] <= array[mid]:
		if target >= array[left] and target < array[mid]:
			return search(array, left, mid-1, target)
		else:
			return search(array, mid+1, right, target)
	# Right is in order
	else:
		if target > array[mid] and target <= array[right]:
			return search(array, mid+1, right, target)
		else:
			return search(array, left, mid-1, target)
	
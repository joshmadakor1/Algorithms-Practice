'''
    Binary Search:
    Given a sorted array and target value as input, perform a binary
    search to find the index of the target value. Return the index

    Time:  O(log(N)), where N = number of nodes in array
    Space: O(1)
    
    Last Practice: 2022-03-18 06:59:27
'''
def binarySearch(array, target, left=None, right=None):
    if left is None:
        left = 0
        right = len(array) - 1
    if left > right: return -1
    mid = (left + right) // 2
    if target < array[mid]: return binarySearch(array, target, left, mid - 1)
    elif target > array[mid]: return binarySearch(array, target, mid + 1, right)
    elif target == array[mid]: return mid
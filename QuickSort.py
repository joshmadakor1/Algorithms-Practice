'''
    QuickSort:
    Given an input array, perform a quicksort on it and return the sorted array

    Best Time:  O(NlogN), where N are the number of nodes in the list
    Worst Time: O(N^2)
    Space: O(NlogN) due to the recursive call stack 

    Last Practice: 2022-03-17 08:00:54
'''
def quickSort(array, start=None, end=None):
    if start is None and end is None:
        start, end = 0, len(array) - 1
    elif start > end: return
    
    pivot = start
    left = start + 1
    right = end
    
    while left <= right:
        if array[left] > array[pivot] and array[right] < array[pivot]:
            swap(array, left, right)
        if array[left] <= array[pivot]:
            left += 1
        if array[right] >= array[pivot]:
            right -= 1
    swap(array, right, pivot)
    
    leftSubArrayIsSmaller = (right - 1 - start) < (end - (right + 1))
    
    if leftSubArrayIsSmaller:
        quickSort(array, start, right - 1)
        quickSort(array, right + 1, end)
    else:
        quickSort(array, right + 1, end)
        quickSort(array, start, right - 1)
    
    return array
            
def swap(array, left, right):
    array[left], array[right] = array[right], array[left]
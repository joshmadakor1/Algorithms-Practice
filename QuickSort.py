'''
    QuickSort:
    Given an input array, perform a quicksort on it and return the sorted array

    Best Time:  O(NlogN), where N are the number of nodes in the list
    Worst Time: O(N^2)
    Space: O(NlogN) due to the recursive call stack 

    Last Practice: 2022-03-26 07:54:58
'''
def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array

def quickSortHelper(array, start, end):
    if start > end: return
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

    leftSubArrayIsSmaller = ((right - 1) - left) < (end - (right + 1))

    if leftSubArrayIsSmaller:
        quickSortHelper(array, start, right - 1)
        quickSortHelper(array, right + 1, end)
    else:
        quickSortHelper(array, right + 1, end)
        quickSortHelper(array, start, right - 1)

def swap(array, left, right):
    array[left], array[right] = array[right], array[left]

print(quickSort([9,8,7,6,5,4,3,2,1,0,-1,-2]))
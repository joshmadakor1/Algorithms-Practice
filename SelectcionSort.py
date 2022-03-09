'''
    SelectionSort:
    Given an unsorted array as input, perform a SelectionSort and
    return the sorted array

    Time: O(N^2), where N = number of nodes in array
    Space: O(1)

    Last Practice: 2022-03-09 08:57:15
'''
def selectionSort(array):
    for i in range(len(array)):
        smallestIndex = i
        for j in range(i, len(array)):
            if array[j] < array[smallestIndex]:
                smallestIndex = j
        swap(array, i, smallestIndex)
    return array

def swap(array, left, right):
    array[left], array[right] = array[right], array[left]
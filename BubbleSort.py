'''
    BubbleSort:
    Given an unsorted array as input, perform a BubbleSort and
    return the sorted array

    Average Time: O(N^2), where N = number of nodes in array
    Best Time: O(N), where the array is already sorted
    Space: O(1)

    Last Practiced: 2022-03-14 08:22:36
'''
def bubbleSort(array):
    isSorted = False
    index = 0
    while not isSorted:
        isSorted = True
        for i in range(1, len(array) - index):
            if array[i] < array[i-1]:
                swap(array, i, i-1)
                isSorted = False
        index += 1
    return array

def swap(array, left, right):
    array[left], array[right] = array[right], array[left]
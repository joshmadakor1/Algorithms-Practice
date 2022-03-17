'''
    SelectionSort:
    Given an unsorted array as input, perform a SelectionSort and
    return the sorted array

    Time: O(N^2), where N = number of nodes in array
    Space: O(1)

    Last Practice: 2022-03-17 08:05:53
'''
def insertionSort(array):
    for i in range(len(array)-1):
        smallestIndex = i
        for j in range(i+1, len(array)):
            if array[j] < array[smallestIndex]:
                smallestIndex = j
        array[i], array[smallestIndex] = array[smallestIndex], array[i]
    return array
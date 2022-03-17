'''
    Insertion Sort:
    Given an unsorted array as input, perform an Insertion Sort and
    return the sorted array

    Average Time: O(N^2), where N = number of nodes in array
    Best Time: O(N), when the array is already sorted
    Space: O(1)

    Last Practiced: 2022-03-17 08:18:06
'''
def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array
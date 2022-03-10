'''
    Insertion Sort:
    Given an unsorted array as input, perform an Insertion Sort and
    return the sorted array

    Average Time: O(N^2), where N = number of nodes in array
    Best Time: O(N), when the array is already sorted
    Space: O(1)

    Last Practiced: 2022-03-10 07:49:51
'''
def insertionSort(array):
    for i in range(1, len(array)):
        count = i
        while count > 0 and array[count] < array[count - 1]:
            swap(array, count, count - 1)
            count -= 1
    return array
            
def swap(array, left, right):
    array[left], array[right] = array[right], array[left]

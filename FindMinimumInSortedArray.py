'''
    Find Minimum In Sorted Array:
    Time: O(N)
    Space: O(1)
'''
def findMinInSortedArray(array):
    currentMin = array[0]
    count = 0

    for i, element in enumerate(array):
        count += 1
        print("count", count)
        currentMin = min(currentMin, element)
        if i > 0:
            if array[i-1] > array[i]:
                return currentMin
    return currentMin



print(findMinInSortedArray([3,4,5,1,2]))
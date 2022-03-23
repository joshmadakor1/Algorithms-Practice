'''
    Move Element To End:
    Given an input array and an input value, move all elements
    that are equal to the input value to the end of the array

    Time: O(N), where N is the number of elements in the array
    Space: O(1), mutate existing array

    Last Practiced: 2022-03-23 07:24:42
'''
def moveElementToEnd(array, toMove):
    left = 0
    right = len(array) - 1
    
    while left < right:
        while array[right] == toMove and left < right:
            right -= 1
        if array[left] == toMove:
            array[left], array[right] = array[right], array[left]
        left += 1
    
    return array

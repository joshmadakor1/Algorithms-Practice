'''
    First Duplicate Value:
    Given an array, return the instance of the first duplicate value.
    If there are no duplicate values, return -1

    Time: O(N), where N is the number of elements in the array
    Space: O(N), where N is the number of elements in the array

    Last Practice: 2022-03-12 23:33:35
'''
def firstDuplicateValue(array):
    values = {} # Will hold values "so far" while iterating through array

    for element in array:
        if element in values: return element
        else: values[element] = element
    return -1
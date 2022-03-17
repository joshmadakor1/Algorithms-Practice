'''
    Product Sum:
    Write a function that takes in a special array which contains
    integers and other nested arrays of integers. The product sum
    is the sum of the arrays elements, multiplied by the level of
    the depth of the nested arrays.

    Time:  O(N) - Linear
    Space: O(D) -> O(N), where D is the depth of the recursive call stack - Linear
'''
def productSum(array, depth = 1):
    sum = 0
    for element in array:
        if type(element) == type([]):
            sum += productSum(element, depth + 1)
        else:
            sum += element
    return sum * depth


assert productSum([5, 1, [7, -1], 3, [6, [-13, 8], 4]]) == 11, "Error. Expected output: 11"
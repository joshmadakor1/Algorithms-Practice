'''
    Three Number Sum:
    Take in an array and a target value. return all the sets of
    three numbers from within the array that sum up to the target value

    Time:  O(N^2) - Exponential
    Space: O(N)   - Linear

    Last Practiced: 2022-03-15 07:44:50
'''
def threeNumberSum(array, targetSum):
    array.sort()
    sums = []
    for i in range(len(array)):
        left = i + 1
        right = len(array) - 1
        while left < right:
            if sum(array, i, left, right) == targetSum:
                sums.append(makeArray(array, i, left, right))
                left += 1
                right -= 1
            elif sum(array, i, left, right) < targetSum:
                left += 1
            elif sum(array, i, left, right) > targetSum:
                right -= 1
    return sums

def sum(array, i, left, right):
    return array[i] + array[left] + array[right]

def makeArray(array, i, left, right):
    return [array[i], array[left], array[right]]


assert threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0) == [[-8, 2, 6],[-8, 3, 5],[-6, 1, 5]], "Error. Expected output: [[-8, 2, 6],[-8, 3, 5],[-6, 1, 5]]"
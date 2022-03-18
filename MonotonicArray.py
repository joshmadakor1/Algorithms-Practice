'''
    Monotonic Array:
    Write a function that takes in an array of integers and return 
    True if the numbers are sequentially increase, decreasing, or
    staying consistent. Return False if the numbers "change direction."
    Example:

    [0,1,1,1,2,3,10,15] -> returns True
    [0,0,0,-1,1] -> returns False

    Time:  O(N), The length of the input array is iterated once
    Space: O(1)

    Last Practiced: 2022-03-18 06:22:27
'''
def isMonotonic(array):
    if len(array) < 3: return True
    currentDirection = array[1] - array[0]
    for i in range(2, len(array)):
        if currentDirection == 0:
            currentDirection = array[i] - array[i-1]
            continue
        if changesDirection(currentDirection, array[i] - array[i-1]):
            return False
    return True

def changesDirection(currentDirection, nextDirection):
    if currentDirection < 0:
        return nextDirection > 0
    return nextDirection < 0
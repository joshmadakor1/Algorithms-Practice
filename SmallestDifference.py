'''
    Smallest Difference:
    Given two separate arrays, find two elements (one from each array) where
    their difference is closest to zero(0). Return an array containing the two
    numbers.

    Time:  O(nlog(n) + mlog(m)) where n and m are the lengths of the arrays
    Space: O(1)
'''
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    pointerOne = 0
    pointerTwo = 0
    currentSmallest = float("inf")
    answer = []
    candidate = 0
    
    while pointerOne < len(arrayOne) and pointerTwo < len(arrayTwo):
        candidate = abs(arrayOne[pointerOne] - arrayTwo[pointerTwo])
        if candidate < currentSmallest:
            currentSmallest = candidate
            answer = [arrayOne[pointerOne], arrayTwo[pointerTwo]]
        if arrayOne[pointerOne] < arrayTwo[pointerTwo]:
            pointerOne += 1
        elif arrayTwo[pointerTwo] < arrayOne[pointerOne]:
            pointerTwo += 1
        else:
            break
            
    return answer

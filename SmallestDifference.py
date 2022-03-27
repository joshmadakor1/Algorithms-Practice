'''
    Smallest Difference:
    Given two separate arrays, find two elements (one from each array) where
    their difference is closest to zero(0). Return an array containing the two
    numbers.

    Time:  O(nlog(n) + mlog(m)) where n and m are the lengths of the arrays
    Space: O(1)

    Last Practiced: 2022-03-27 05:58:38
'''
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    
    pointerOne = 0
    pointerTwo = 0
    
    currentSmallestDiff = abs(arrayOne[0] - arrayTwo[0])
    currentSmallsetPair = [arrayOne[0], arrayTwo[0]]
    
    while pointerOne < len(arrayOne) and pointerTwo < len(arrayTwo):
        
        candidateSmallestDiff = abs(arrayOne[pointerOne] - arrayTwo[pointerTwo])
        
        if candidateSmallestDiff == 0:
            return [arrayOne[pointerOne], arrayTwo[pointerTwo]]
        
        elif candidateSmallestDiff < currentSmallestDiff:
            currentSmallestDiff = candidateSmallestDiff
            currentSmallsetPair = [arrayOne[pointerOne], arrayTwo[pointerTwo]]
        
        if arrayOne[pointerOne] < arrayTwo[pointerTwo]:
            pointerOne += 1
        else:
            pointerTwo += 1
            
    return currentSmallsetPair

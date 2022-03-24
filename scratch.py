def waterArea(heights):
    numberOfSlots = len(heights)
    maxFromLeft = [0] * numberOfSlots
    maxFromRight = [0] * numberOfSlots
    totalArea = 0

    currentMaxSoFar = 0
    for i in range(len(heights)):
        maxFromLeft[i] = currentMaxSoFar
        currentMaxSoFar = max(currentMaxSoFar, heights[i])
    
    currentMaxSoFar = 0
    for i in reversed(range(len(heights))):
        maxFromRight[i] = currentMaxSoFar
        currentMaxSoFar = max(currentMaxSoFar, heights[i])
    
    for i in range(len(heights)):
        minPillarHeight = min(maxFromLeft[i], maxFromRight[i])
        if minPillarHeight > heights[i]:
            totalArea += (minPillarHeight - heights[i])
    
    return totalArea


waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3])

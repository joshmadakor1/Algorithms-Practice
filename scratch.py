def waterArea(heights):
    largestLeft = [0] * len(heights)
    largestRight = [0] * len(heights)
    
    largestSoFar = 0
    for i in range(len(heights)):
        largestLeft [i]= largestSoFar
        largestSoFar = max(heights[i], largestSoFar)
    
    largestSoFar = 0
    for i in reversed(range(len(heights))):
        largestRight[i] = largestSoFar
        largestSoFar = max(heights[i], largestSoFar)
        
    totalArea = 0

    for i in range(len(heights)):
        walls = min(largestLeft[i], largestRight[i])
        if heights[i] < walls:
            totalArea += walls - heights[i]

    return totalArea

    
waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3])
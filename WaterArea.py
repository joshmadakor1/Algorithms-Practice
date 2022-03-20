'''
    Water Area:
    Water Pillar Problem, hard to explain, lol:
    https://www.algoexpert.io/questions/Water%20Area

    Time: O(N^2)
    Space: O(N)

    Needs to be optimized

    Last Practiced: 2022-03-20 07:40:00
'''
def waterArea(heights):
    areaPerIndex = [0] * len(heights)
    totalArea = 0
    
    for i in range(1,len(heights)-1):
        largestLeftIndex, largestRightIndex = getLargetLeftAndRightIndex(heights, i)
        if heights[largestLeftIndex] < heights[i] or heights[largestRightIndex] < heights[i]:
            areaPerIndex[i] = 0
        else:
            areaAtCurrentIndex = min(heights[largestLeftIndex],heights[largestRightIndex]) - heights[i]
            areaPerIndex[i] = areaAtCurrentIndex
            totalArea += areaAtCurrentIndex
    return totalArea

def getLargetLeftAndRightIndex(heights, index):
    left = index - 1
    largestLeftValue = 0
    largestLeftIndex = 0
    right = index + 1
    largestRightValue = 0
    largestRightIndex = 0
    
    while left > 0:
        if heights[left] > largestLeftValue:
            largestLeftValue = heights[left]
            largestLeftIndex = left
        left -= 1
            
    while right < len(heights):
        if heights[right] > largestRightValue:
            largestRightValue = heights[right]
            largestRightIndex = right
        right += 1
    
    return largestLeftIndex, largestRightIndex

print(waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
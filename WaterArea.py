'''
    Water Area:
    Water Pillar Problem, hard to explain, lol:
    https://www.algoexpert.io/questions/Water%20Area

    Time: O(3N) -> O(N)
    Space: O(N)

    Last Practiced: 2022-03-24 08:36:14
'''
def waterArea(heights):
    largestToTheLeft = [0] * len(heights)
    largestToTheRight = [0] * len(heights)
    totalArea = 0
    
    # Calculate largest to the left of each pillar
    largestSoFar = 0
    for i in range(len(heights)):
        largestToTheLeft[i] = largestSoFar
        largestSoFar = max(largestSoFar, heights[i])
    
    # Calculate largest to the right of each pillar
    largestSoFar = 0
    for i in reversed(range(len(heights))):
        largestToTheRight[i] = largestSoFar
        largestSoFar = max(largestSoFar, heights[i])
        
    for i in range(len(heights)):
        surroundingPillarHeights = min(largestToTheLeft[i],largestToTheRight[i])
        if heights[i] < surroundingPillarHeights:
            totalArea += surroundingPillarHeights - heights[i]
    
    return totalArea
            


    
waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3])

# def waterArea(heights):
#     areaPerIndex = [0] * len(heights)
#     totalArea = 0
    
#     for i in range(1,len(heights)-1):
#         largestLeftIndex, largestRightIndex = getLargetLeftAndRightIndex(heights, i)
#         if heights[largestLeftIndex] < heights[i] or heights[largestRightIndex] < heights[i]:
#             areaPerIndex[i] = 0
#         else:
#             areaAtCurrentIndex = min(heights[largestLeftIndex],heights[largestRightIndex]) - heights[i]
#             areaPerIndex[i] = areaAtCurrentIndex
#             totalArea += areaAtCurrentIndex
#     return totalArea

# def getLargetLeftAndRightIndex(heights, index):
#     left = index - 1
#     largestLeftValue = 0
#     largestLeftIndex = 0
#     right = index + 1
#     largestRightValue = 0
#     largestRightIndex = 0
    
#     while left > 0:
#         if heights[left] > largestLeftValue:
#             largestLeftValue = heights[left]
#             largestLeftIndex = left
#         left -= 1
            
#     while right < len(heights):
#         if heights[right] > largestRightValue:
#             largestRightValue = heights[right]
#             largestRightIndex = right
#         right += 1
    
#     return largestLeftIndex, largestRightIndex

# print(waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
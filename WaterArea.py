'''
    Water Area:
    Water Pillar Problem, hard to explain, lol:
    https://www.algoexpert.io/questions/Water%20Area

    Time: O(3N) -> O(N)
    Space: O(N)

    Last Practiced: 2022-03-27 05:26:10
'''
def waterArea(heights):
    leftHighest = [0] * len(heights)
    rightHighest = [0] * len(heights)
    totalArea = 0
    
    currentHighest = 0
    for i in range(len(heights)):
        leftHighest[i] = currentHighest
        currentHighest = max(currentHighest, heights[i])
        
    currentHighest = 0
    for i in reversed(range(len(heights))):
        rightHighest[i] = currentHighest
        currentHighest = max(currentHighest, heights[i])
        
    for i in range(len(heights)):
        wallSize = min(leftHighest[i], rightHighest[i])
        if wallSize > heights[i]: totalArea += (wallSize - heights[i])
    
    return totalArea

print(waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
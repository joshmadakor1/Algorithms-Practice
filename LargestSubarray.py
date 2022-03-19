'''
    LargestSubarray

    Time: O(N)
    Space: O(1)

    Last Practiced: 2022-03-19 09:02:23
'''
def largesSubarray(array):
    currentLargest = float('-inf')
    for i in range(len(array)):
        currentSum = 0
        if i < 0: continue
        for j in range(i,len(array)):
            currentSum += array[j]
            if currentSum > currentLargest:
                currentLargest = currentSum
    return currentLargest

print(largesSubarray([-2,1,-3,4,-1,2,1,-5,4]))
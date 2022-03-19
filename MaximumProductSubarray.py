def maximumProductSubarray(array):
    count = 0
    maxProduct = float('-inf')
    for i in range(len(array)):
       currentProduct = 1
       for j in range(i,len(array)):
           count+=1
           print("count",count)
           currentProduct *= array[j]
           maxProduct = max(maxProduct,currentProduct)
    return maxProduct

'''
    Optimal:
    Time: O(N)
    Space: O(1)

    Last Practiced: 2022-03-19 09:02:17
'''
def maximumProductSubarray2(array):
    currentMax, currentMin = 1,1
    resultMax = float('-inf')
    for element in array:
        if element == 0:
            currentMax, currentMin = 1,1
            continue
        oldMax = currentMax
        currentMax = max(element * currentMax, element * currentMin, element)
        currentMin = min(element* oldMax, element* currentMin, element)
        resultMax = max(currentMax, currentMin, resultMax)

    return max(currentMax, resultMax)

def maxProdSubArray(array):
    currentMax, currentMin, maxResult = 1,1,1
    for element in array:
        if element == 0:
            currentMax, currentMin = 1,1
            continue
        oldMax = currentMax
        currentMax = max(currentMax * element, currentMin * element, element)
        currentMin = min(oldMax * element, currentMin * element, element)
        maxResult = max(maxResult, currentMax)
    return max(maxResult, currentMax)


print(maxProdSubArray([2,3,-2,4]))
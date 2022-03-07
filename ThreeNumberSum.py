
'''
	Three Number Sum:
	Take in an array and a target value. return all the sets of
    three numbers from within the array that sum up to the target value

	Time:  O(N^2) - Exponential
	Space: O(N)   - Linear
'''
def threeNumberSum(array, targetSum):
    threeNumberSums = []
    array.sort()
    
    for i in range(len(array)):
        left = i + 1
        right = len(array) - 1
        
        while left < right:
            candidateSum = sum(array, i, left, right)
            if candidateSum == targetSum:
                threeNumberSums.append(makeArray(array, i, left, right))
                left += 1
                right -= 1
            elif candidateSum > targetSum:
                right -= 1
            elif candidateSum < targetSum:
                left += 1
    
    return threeNumberSums
            
def sum(array, i, left, right):
    return array[i] + array[left] + array[right]

def makeArray(array, i, left, right):
    return [array[i], array[left], array[right]]

assert threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0) == [[-8, 2, 6],[-8, 3, 5],[-6, 1, 5]], "Error. Expected output: [[-8, 2, 6],[-8, 3, 5],[-6, 1, 5]]"
'''
    Single Cycle Check:

    Consider an array of integers where each integer represents a jump of its value
    in the array. If a jump spills past either bounds, it will wrap around to the 
    other side of the array. Write a function that determines whether the jumps form
    a single cycle or not. A cycle occurs if starting at any index in the array and
    following the jumps, every element in the array is visited exactly once before 
    landing back on the starting index

    Time:  O(N), where N is the number of elements in the array
    Space: O(C)

    LastPracticed: 2022-03-16 08:58:52
'''
def hasSingleCycle(array):
	currentIndex = 0
	for i in range(len(array)):
		if currentIndex == 0 and i > 0: return False
		currentIndex = getNextIndex(array, currentIndex)
	return currentIndex == 0

def getNextIndex(array, currentIndex):
	return (currentIndex + array[currentIndex]) % len(array)

assert hasSingleCycle([2, 3, 1, -4, -4, 2]) == True, "Error. Expected output: True"
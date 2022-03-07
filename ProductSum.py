'''
	Product Sum:
	Write a function that takes in a special array which contains
	integers and other nested arrays of integers. The product sum
	is the sum of the arrays elements, multiplied by the level of
	the depth of the nested arrays.
'''
def productSum(array):
    rootDepth = 1
    return calculateProductSum(array, rootDepth)

def calculateProductSum(array, depth):
	sum = 0
	for element in array:
		if type(element) == type([]):
			sum += calculateProductSum(element, depth + 1)
		else:
			sum += element
	return sum * depth

assert productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]) == 12, print("Error. Expected output: ", 12)
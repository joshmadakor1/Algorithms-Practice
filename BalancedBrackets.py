'''
    Balanced Brackets:
    Write a function that takes in a string containing brackets: ({[]})
    as well as other alphabet characters and returns True if the brackets
    are balanced, and False if not. For example:

    Balanced: (()(){x}[a]{{{()}()}})
    Unbalanced: (([)){

    Time:  O(N), The length of the input array is iterated once
    Space: O(N), The stack holding the characters
'''
def balancedBrackets(string):
	bracketPairs = {'}':'{', ']':'[', ')':'('}
	openingBrackets = "{[("
	closingBrackets = "}])"
	stack = []
	
	for character in string:
		if len(stack) == 0 and character in closingBrackets:
			return False
		if character in openingBrackets:
			stack.append(character)
		elif character in closingBrackets:
			if bracketPairs[character] == stack[-1]:
				stack.pop()
			else:
				return False
	if len(stack) == 0:
		return True
	return False
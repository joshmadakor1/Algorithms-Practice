'''
    Balanced Brackets:
    Write a function that takes in a string containing brackets: ({[]})
    as well as other alphabet characters and returns True if the brackets
    are balanced, and False if not. For example:

    Balanced: (()(){x}[a]{{{()}()}})
    Unbalanced: (([)){

    Time:  O(N), The length of the input array is iterated once
    Space: O(N), The stack holding the characters

	Last Practiced: 2022-03-16 07:59:08
'''
def balancedBrackets(string):
    leftBrackets = '({['
    rightBrackets = ']})'
    bracketMap = {')':'(', '}': '{', ']':'['}
    stack = []
    
    for char in string:
        if char in rightBrackets:
            if stackIsEmpty(stack): return False
            if bracketMap[char] == stack[-1]: stack.pop()
            else: return False
        if char in leftBrackets:
            stack.append(char)
    return stackIsEmpty(stack)
        
        
def stackIsEmpty(stack):
    return len(stack) == 0

'''
	Palindrome Check:
	Write a function that takes in a a string and determines whether it
    is a palindrome or not. (Reads the same forward vs backwards.
    For ex: "racecar")

	Time:  O(N) - Linear
	Space: O(1) - Constant
'''
def isPalindrome(string):
	left = 0
	right = len(string) - 1
	while left < right:
		if not string[left] == string[right]:
			return False
		left += 1
		right -= 1
	return True

assert isPalindrome("xcabcdcbacx") == True, "Error. Expected output: True"
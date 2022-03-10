'''
	Find Three Largest Numbers:
	Given an input array, find the three largest numbers
    in the array and return them in an array of their own,
    in sorted order. Example:

    Input:  [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    Output: [18, 141, 541]

    Time:  O(N)
    Space: O(1)

	Last Practiced: 2022-03-10 07:33:22
'''
def findThreeLargestNumbers(array):
    answer = [None] * 3
    for element in array:
        insert(answer, element)
    return answer

def insert(answer, number):
    if answer[2] is None or number > answer[2]:
        shift(answer, number, 2)
    elif answer[1] is None or number > answer[1]:
        shift(answer, number, 1)
    elif answer[0] is None or number > answer[0]:
        answer[0] = number
    
def shift(answer, number, index):
    count = 0
    while count <= index:
        if count < index:
            answer[count] = answer[count+1]
        else:
            answer[count] = number
        count += 1
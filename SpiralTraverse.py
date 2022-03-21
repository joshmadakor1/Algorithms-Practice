'''
    Spiral Traverse:
    Write a function that takes in a matrix (2d-array),
    traverse the array in a clockwise spiral starting at element [0][0].
    for each element visited, append the value to an array and return
    the array

    Time:  O(N), where N is the number of nodes in the matrix
    Space: O(N), where N is the number of nodes in the matrix

    Last Practice: 2022-03-21 07:40:19
'''
def spiralTraverse(array):
    answer = []
    startCol = 0
    endCol = len(array[0]) -1
    startRow = 0
    endRow = len(array) - 1
    
    while startRow <= endRow and startCol <= endCol:
        
        for col in range(startCol, endCol + 1):
            answer.append(array[startRow][col])
        for row in range(startRow + 1, endRow + 1):
            answer.append(array[row][endCol])
        for col in reversed(range(startCol, endCol)):
            if startRow != endRow:
                answer.append(array[endRow][col])
        for row in reversed(range(startRow + 1, endRow)):
            if startCol != endCol:
                answer.append(array[row][startCol])
        
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -=1
        
    return answer



spiralTraverse([
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
  ])
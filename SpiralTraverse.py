'''
    Spiral Traverse:
    Write a function that takes in a matrix (2d-array),
    traverse the array in a clockwise spiral starting at element [0][0].
    for each element visited, append the value to an array and return
    the array

    Time:  O(N), where N is the number of nodes in the matrix
    Space: O(N), where N is the number of nodes in the matrix

    Last Practice: 2022-03-12 23:45:22
'''
def spiralTraverse(array):
    unrolledMatrix = []
    rowStart = 0
    rowEnd = len(array) - 1
    colStart = 0
    colEnd = len(array[0]) - 1
    
    while rowStart <= rowEnd and colStart <= colEnd:
        for col in range(colStart, colEnd + 1):
            unrolledMatrix.append(array[rowStart][col])
        for row in range(rowStart + 1, rowEnd + 1):
            unrolledMatrix.append(array[row][colEnd])
        for col in reversed(range(colStart, colEnd)):
            if rowStart != rowEnd:
                unrolledMatrix.append(array[rowEnd][col])
        for row in reversed(range(rowStart + 1, rowEnd)):
            if colStart != colEnd:
                unrolledMatrix.append(array[row][colStart])
        
        rowStart += 1
        rowEnd -= 1
        colStart += 1
        colEnd -= 1
        
    return unrolledMatrix
spiralTraverse([
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
  ])
'''
    River Sizes:
    Given a 2d array (matrix) of 1s and 0s return an array that contains
    the sizes of the "rivers" within the matrix". A "river" is any
    number of 1s that are either horizontally or vertically adjacent.
    The following matrix contains two rivers of length 2 and 7:

    0 0 0 0 1
    0 1 0 1 1
    0 1 0 1 0
    0 0 0 1 0
    0 0 0 1 1

    Time:  O(width * height) => O(N), where N is the number of elements in the matrix
    Space: O(width * height) => O(N), where N is the number of elements in the matrix (aux matrix)

    Last Practiced: 2022-03-16 08:23:51
'''
def riverSizes(matrix):
    riverSizes = []
    visited = [[False for value in row] for row in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if visited[row][col]: continue
            else: traverseRiverNodes(row, col, matrix, visited, riverSizes)
    return riverSizes
    
def traverseRiverNodes(row, col, matrix, visited, riverSizes):
    currentRiverSize = 0
    nodesToVisit = [[row,col]]
    while len(nodesToVisit):
        currentNode = nodesToVisit.pop()
        currentRow = currentNode[0]
        currentCol = currentNode[1]
        
        if visited[currentRow][currentCol]: continue
        visited[currentRow][currentCol] = True
        if matrix[currentRow][currentCol] == 0: continue
        currentRiverSize += 1
        
        neighbors = getNeighbors(currentRow, currentCol, matrix, visited)
        for neighbor in neighbors:
            nodesToVisit.append(neighbor)
            
    if currentRiverSize > 0: riverSizes.append(currentRiverSize)

def getNeighbors(row, col, matrix, visited):
    nodesToVisit = []
    
    if row > 0 and not visited[row-1][col]:
        nodesToVisit.append([row-1, col])
    if row < len(matrix) - 1 and not visited[row+1][col]:
        nodesToVisit.append([row+1, col])
    if col > 0 and not visited[row][col-1]:
        nodesToVisit.append([row,col-1])
    if col < len(matrix[row]) -1 and not visited[row][col+1]:
        nodesToVisit.append([row,col+1])
    
    return nodesToVisit
    

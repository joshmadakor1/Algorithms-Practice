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

    Last Practiced: 2022-03-15 06:36:52
'''
def riverSizes(matrix):
    visitedNodes = [[False for value in row] for row in matrix]
    riverSizes = []
    
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if visitedNodes[row][col]:
                continue
            traverseRiver(row, col, matrix, visitedNodes, riverSizes)
    
    return riverSizes
            
def traverseRiver(row, col, matrix, visitedNodes, riverSizes):
    currentRiverSize = 0
    nodesToExplore = [[row, col]]
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        currentRow = currentNode[0]
        currentCol = currentNode[1]
        if visitedNodes[currentRow][currentCol]:
            continue
        visitedNodes[currentRow][currentCol] = True
        if matrix[currentRow][currentCol] == 0:
            continue
        currentRiverSize += 1
        unvisitedNodes = getNeighborNodes(currentRow, currentCol, matrix, visitedNodes)
        for unvisitedNode in unvisitedNodes:
            nodesToExplore.append(unvisitedNode)
    if currentRiverSize > 0:
        riverSizes.append(currentRiverSize)
    
def getNeighborNodes(row, col, matrix, visitedNodes):
    neighbors = []
    
    if row > 0 and not visitedNodes[row-1][col]:
        neighbors.append([row-1,col])
    if row < len(matrix) - 1 and not visitedNodes[row+1][col]:
        neighbors.append([row+1,col])
    if col > 0 and not visitedNodes[row][col-1]:
        neighbors.append([row,col-1])
    if col < len(matrix[0]) - 1 and not visitedNodes[row][col+1]:
        neighbors.append([row,col+1])
    
    return neighbors

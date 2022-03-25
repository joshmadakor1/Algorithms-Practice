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

    Last Practiced: 2022-03-25 05:39:38
'''
def riverSizes(matrix):
    visited = [[False for value in row] for row in matrix]
    sizes = []
    
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if not visited[row][col]:
                traversRiver(matrix, row, col, visited, sizes)
    return sizes

def traversRiver(matrix, row, col, visited, sizes):
    currentRiverSize = 0
    nodesToVisit = [[row,col]]
    while len(nodesToVisit):
        currentNode = nodesToVisit.pop()
        currentRow = currentNode[0]
        currentCol = currentNode[1]
        if visited[currentRow][currentCol]:
            continue
        visited[currentRow][currentCol] = True
        if matrix[currentRow][currentCol] == 0:
            continue
        currentRiverSize += 1
        neighbors = getNeighboringNodes(matrix, currentRow, currentCol, visited)
        for neighbor in neighbors:
            nodesToVisit.append(neighbor)
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)

def getNeighboringNodes(matrix, row, col, visited):
    neighbors = []
    if row > 0 and not visited[row-1][col]:
        neighbors.append([row-1, col])
    if row < len(matrix) - 1 and not visited[row+1][col]:
        neighbors.append([row+1, col])
    if col > 0 and not visited[row][col-1]:
        neighbors.append([row, col-1])
    if col < len(matrix[row])-1 and not visited[row][col+1]:
        neighbors.append([row, col+1])
    return neighbors
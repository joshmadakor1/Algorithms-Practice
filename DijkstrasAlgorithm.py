'''
    Dijkstra's Algorithm:
    Write a function that takes in an adjacency list and a starting index.
    Use Dijkstra's algorithm to find the shortest path to each vertex
    in the adjacency list and return the shortest distance to each node
    as an array (list). If a node is unreachable, it will have a distance
    of -1. Example:

    Input:  [[[1,7]],[[2,6],[3,20],[4,3]],[[3,14]],[[4,2]],[],[]]
    Output: [0, 7, 13, 27, 10, -1]

    Time:  
    Space: 
    
    Last Practice: 2022-03-14 06:53:42
'''
def dijkstrasAlgorithm(start, edges):
    numberOfVerticies = len(edges)
    minDistancesToEachVertexFromStart = [float('inf')] * numberOfVerticies
    minDistancesToEachVertexFromStart[start] = 0
    visitedNodes = set()

    while thereAreStillNodesToVisit(visitedNodes, numberOfVerticies):
        currentVertex, distanceFromStartToCurrentVertex = getVertexWithMinDistanceThatHasntBeenVisited(minDistancesToEachVertexFromStart, visitedNodes)
        if distanceFromStartToCurrentVertex == float('inf'):
            break
        visitedNodes.add(currentVertex)

        for edge in edges[currentVertex]:
            currentVertexNeighbor, distanceFromCurrentVertexToCurrentVertexNeighbor = edge

            if currentVertexNeighbor in visitedNodes:
                continue

            newDistanceFromStartToCurrentVertexNeighbor = distanceFromStartToCurrentVertex + distanceFromCurrentVertexToCurrentVertexNeighbor
            currentDistanceFromStartToCurrentVertexNeighbor = minDistancesToEachVertexFromStart[currentVertexNeighbor]
            
            if newDistanceFromStartToCurrentVertexNeighbor < currentDistanceFromStartToCurrentVertexNeighbor:
                minDistancesToEachVertexFromStart[currentVertexNeighbor] = newDistanceFromStartToCurrentVertexNeighbor
    # End while
    return list(map(lambda x: -1 if x == float('inf') else x, minDistancesToEachVertexFromStart))

def thereAreStillNodesToVisit(visitedNodes, numberOfVerticies):
    return len(visitedNodes) < numberOfVerticies

def getVertexWithMinDistanceThatHasntBeenVisited(minDistancesToEachVertexFromStart, visitedNodes):
    currentMinDistance = float('inf')
    currentVertex = -1

    for vertex, distance in enumerate(minDistancesToEachVertexFromStart):
        if vertex in visitedNodes:
            continue
        if distance <= currentMinDistance:
            currentMinDistance = distance
            currentVertex = vertex

    return currentVertex, currentMinDistance

distances = [[[1,7]],[[2,6],[3,20],[4,3]],[[3,14]],[[4,2]],[],[]]
start = 0

print(dijkstrasAlgorithm(start, distances))
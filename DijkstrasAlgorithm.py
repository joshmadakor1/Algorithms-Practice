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
    
    Last Practice: 2022-03-14 07:07:14
'''
def dijkstrasAlgorithm(start, edges):
    numberOfVerticies = len(edges)
    minDistanceToEachVertexFromStart = [float('inf')] * numberOfVerticies
    minDistanceToEachVertexFromStart[start] = 0
    visitedNodes = set()

    while thereAreStillNodesToVisit(visitedNodes, numberOfVerticies):
        currentVertex, distanceFromStartToCurrentVertex = getVertexWithMinDistanceThatHasntBeenVisited(minDistanceToEachVertexFromStart, visitedNodes)

        if distanceFromStartToCurrentVertex == float('inf'):
            break

        visitedNodes.add(currentVertex)

        for edge in edges[currentVertex]:
            currentVertexNeighbor, distanceFromCurrentVertexToCurrentVertexNeighbor = edge
            
            if currentVertexNeighbor in visitedNodes:
                continue

            newDistanceFromStartToCurrentVertexNeighbor = distanceFromStartToCurrentVertex + distanceFromCurrentVertexToCurrentVertexNeighbor
            currentDistanceFromStartToCurrentVertexNeighbor = minDistanceToEachVertexFromStart[currentVertexNeighbor]

            if newDistanceFromStartToCurrentVertexNeighbor < currentDistanceFromStartToCurrentVertexNeighbor:
                minDistanceToEachVertexFromStart[currentVertexNeighbor] = newDistanceFromStartToCurrentVertexNeighbor

    return list(map(lambda x: -1 if x == float('inf') else x, minDistanceToEachVertexFromStart))

def getVertexWithMinDistanceThatHasntBeenVisited(minDistancesToEachVertexFromStart, visitedNodes):
    currentVertex = -1
    currentMinDistnace = float('inf')

    for vertex, distance in enumerate(minDistancesToEachVertexFromStart):
        if vertex in visitedNodes:
            continue
        if distance <= currentMinDistnace:
            currentVertex = vertex
            currentMinDistnace = distance
            
    return currentVertex, currentMinDistnace

def thereAreStillNodesToVisit(visitedNodes, numberOfVerticies):
    return len(visitedNodes) < numberOfVerticies

distances = [[[1,7]],[[2,6],[3,20],[4,3]],[[3,14]],[[4,2]],[],[]]
start = 0

print(dijkstrasAlgorithm(start, distances))
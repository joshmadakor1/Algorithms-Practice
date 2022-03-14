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
    
    Last Practice: 2022-03-14 07:22:43
'''
def dijkstrasAlgorithm(start, edges):
    numberOfVerticies = len(edges)
    minDistanceToEachVertexFromStart = [float('inf')] * numberOfVerticies
    minDistanceToEachVertexFromStart[start] = 0
    visitedNodes = set()

    while thereAreStillNodesToVisit(visitedNodes, numberOfVerticies):
        currentVertexBeingVisited, distanceFromStartToCurrentVertexBeingVisited = getVertexWithMinDistanceThatHasntBeenVisited(minDistanceToEachVertexFromStart, visitedNodes)

        if distanceFromStartToCurrentVertexBeingVisited == float('inf'):
            break # The first discovered node where there is no path, algorithm is finished

        visitedNodes.add(currentVertexBeingVisited)

        for edge in edges[currentVertexBeingVisited]:
            currentVertexNeighbor, distanceFromCurrentVertexToCurrentVertexNeighbor = edge

            if currentVertexNeighbor in visitedNodes:
                continue

            newDistanceFromStartToCurrentVertexNeighbor = distanceFromStartToCurrentVertexBeingVisited + distanceFromCurrentVertexToCurrentVertexNeighbor
            currentDistanceFromStartToCurrentVertexNeighbor = minDistanceToEachVertexFromStart[currentVertexNeighbor]

            if newDistanceFromStartToCurrentVertexNeighbor < currentDistanceFromStartToCurrentVertexNeighbor:
                minDistanceToEachVertexFromStart[currentVertexNeighbor] =newDistanceFromStartToCurrentVertexNeighbor
    return list(map(lambda x: -1 if x == float('inf') else x, minDistanceToEachVertexFromStart))

def thereAreStillNodesToVisit(visitedNodes, numberOfVerticies):
    return len(visitedNodes) < numberOfVerticies

def getVertexWithMinDistanceThatHasntBeenVisited(minDistanceToEachVertexFromStart, visitedNodes):
    currentVertex = -1
    currentVertexDistanceFromStart = float('inf')

    for vertex, distance in enumerate(minDistanceToEachVertexFromStart):
        if vertex in visitedNodes:
            continue
        if distance <= currentVertexDistanceFromStart:
            currentVertex = vertex
            currentVertexDistanceFromStart = distance
    return currentVertex, currentVertexDistanceFromStart

distances = [[[1,7]],[[2,6],[3,20],[4,3]],[[3,14]],[[4,2]],[],[]]
start = 0

print(dijkstrasAlgorithm(start, distances))
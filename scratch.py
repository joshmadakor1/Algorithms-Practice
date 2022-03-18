def dijkstrasAlgorithm(start, edges):
    numberOfVerticies = len(edges)
    minDistanceFromStart = [float('inf')] * numberOfVerticies
    minDistanceFromStart[start] = 0
    visited = set()

    while thereAreStillUnvisitedNodes(numberOfVerticies, len(visited)):
        currentVertex, currentVertexDistancFromStart = getNextClosestUnvistedNode(minDistanceFromStart, visited)
        if currentVertexDistancFromStart == float('inf'): break #algorithm finished; next closest node is not reachable
        visited.add(currentVertex)
        for edge in edges[currentVertex]:
            neighborVertex, distanceFromCurrentVertexToNeighborVertex = edge
            if neighborVertex in visited: continue
            newDistanceFromStartToNeighbor = currentVertexDistancFromStart + distanceFromCurrentVertexToNeighborVertex
            currentDistanceFromStartToNeighbor = minDistanceFromStart[neighborVertex]
            if newDistanceFromStartToNeighbor < currentDistanceFromStartToNeighbor:
                minDistanceFromStart[neighborVertex] = newDistanceFromStartToNeighbor
    return list(map(lambda x: -1 if x == float('inf') else x, minDistanceFromStart))

def getNextClosestUnvistedNode(minDistancesFromStart, visited):
    nextVertex = -1
    minDistanceToNextVertex = float('inf')

    for candidateVertext, distance in enumerate(minDistancesFromStart):
        if candidateVertext in visited: continue
        if distance <= minDistanceToNextVertex:
            nextVertex = candidateVertext
            minDistanceToNextVertex = distance
    return [nextVertex, minDistanceToNextVertex]

def thereAreStillUnvisitedNodes(totalNodes, visitedNodes):
    return visitedNodes < totalNodes

distances = [[[1,7]],[[2,6],[3,20],[4,3]],[[3,14]],[[4,2]],[],[]]
start = 0

print(dijkstrasAlgorithm(start, distances))
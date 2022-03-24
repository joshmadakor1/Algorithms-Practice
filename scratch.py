def dijkstrasAlgorithm(edges, start):
    numberOfVertices = len(edges)
    minDistanceFromStart = [float('inf')] * numberOfVertices
    minDistanceFromStart[start] = 0
    visited = set()

    while len(visited) < numberOfVertices:
        currentVertex, currentVertextDistanceFromStart = getNextNearestUnvisitedVertex(minDistanceFromStart, visited)
        if currentVertextDistanceFromStart == float('inf'): break # next nearest node is not reachable
        visited.add(currentVertex)
        for edge in edges[currentVertex]:
            neighborVertex, distanceFromCurrentVertextToNeighbor = edge
            if neighborVertex in visited: continue

            newDistanceFromStartToNeighbor = currentVertextDistanceFromStart + distanceFromCurrentVertextToNeighbor
            currentDistanceFromStartToNeighbor = minDistanceFromStart[neighborVertex]

            if newDistanceFromStartToNeighbor < currentDistanceFromStartToNeighbor:
                minDistanceFromStart[neighborVertex] = newDistanceFromStartToNeighbor
    return list(map(lambda x: -1 if x == float('inf') else x, minDistanceFromStart))

def getNextNearestUnvisitedVertex(minDistanceFromStart, visited):
    candidateVertex = None
    distanceFromStart = float('inf')
    
    for vertex, distance in enumerate(minDistanceFromStart):
        if vertex in visited: continue
        if distance <= distanceFromStart:
            candidateVertex = vertex
            distanceFromStart = distance

    return candidateVertex, distanceFromStart
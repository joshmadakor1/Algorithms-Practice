def dijkstrasAlgorithm(start, edges):
    numberOfVertices = len(edges)
    minDistancesFromStart = [float('inf')] * numberOfVertices
    minDistancesFromStart[start] = 0
    visited = set()

    while len(visited) < numberOfVertices:
        currentVertex, currentVertextDistanceFromStart = getNextClosestUnvisitedVertex(minDistancesFromStart, visited)
        visited.add(currentVertex)
        for edge in edges[currentVertex]:
            currentVertexNeighbor, currentVertexNeighborDistanceFromCurrentVertex = edge
            if currentVertexNeighbor in visited: continue

            newDistanceFromStartToCurrentVertextNeighbor = currentVertextDistanceFromStart + currentVertexNeighborDistanceFromCurrentVertex
            currentDistanceFromStartToCurrentVertexNeighbor = minDistancesFromStart[currentVertexNeighbor]
            
            if newDistanceFromStartToCurrentVertextNeighbor < currentDistanceFromStartToCurrentVertexNeighbor:
                minDistancesFromStart[currentVertexNeighbor] = newDistanceFromStartToCurrentVertextNeighbor

    return list(map(lambda x: -1 if x == float('inf') else x, minDistancesFromStart))


def getNextClosestUnvisitedVertex(minDistancesFromStart, visited):
    nextVertex = -1
    nextVertexDistanceFromStart = float('inf')
    for vertex, distance in enumerate(minDistancesFromStart):
        if vertex in visited: continue
        if distance <= nextVertexDistanceFromStart:
            nextVertex = vertex
            nextVertexDistanceFromStart = distance
    return [nextVertex,nextVertexDistanceFromStart]
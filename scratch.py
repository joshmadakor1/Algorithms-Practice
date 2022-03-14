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
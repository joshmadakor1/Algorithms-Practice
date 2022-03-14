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
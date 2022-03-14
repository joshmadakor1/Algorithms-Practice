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
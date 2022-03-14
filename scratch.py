from calendar import c


def dijkstrasAlgorithm(start, edges):
    numberOfVerticies = len(edges)
    minDistanceFromStartToEachVertex = [float('inf')] * numberOfVerticies
    minDistanceFromStartToEachVertex[start] = 0
    visitedVerticies = set()

    while thereAreStillVerticiesToVisit(visitedVerticies, numberOfVerticies):
        currentVertexBeingVisited, distanceFromStartToCurrentVertexBeingVisited = getVertexWithMinDistanceFromStartThatHasntBeenVisitedYet(minDistanceFromStartToEachVertex, visitedVerticies)

        if distanceFromStartToCurrentVertexBeingVisited == float('inf'):
            break # The first discovered node where there is no path, algorithm is finished

        visitedVerticies.add(currentVertexBeingVisited)

        for edge in edges[currentVertexBeingVisited]:
            currentVertexNeighbor, distanceFromCurrentVertexToCurrentVertexNeighbor = edge

            if currentVertexNeighbor in visitedVerticies:
                continue

            newDistanceFromStartToCurrentVertexNeighbor = distanceFromStartToCurrentVertexBeingVisited + distanceFromCurrentVertexToCurrentVertexNeighbor
            currentDistanceFromStartToCurrentVertexNeighbor = minDistanceFromStartToEachVertex[currentVertexNeighbor]

            if newDistanceFromStartToCurrentVertexNeighbor < currentDistanceFromStartToCurrentVertexNeighbor:
                minDistanceFromStartToEachVertex[currentVertexNeighbor] = newDistanceFromStartToCurrentVertexNeighbor

    return list(map(lambda x: -1 if x == float('inf') else x, minDistanceFromStartToEachVertex))


def getVertexWithMinDistanceFromStartThatHasntBeenVisitedYet(minDistanceFromStartToEachVertex, visitedVerticies):
    currentVertex = -1
    currentDistanceFromStart = float('inf')

    for vertex, distance in enumerate(minDistanceFromStartToEachVertex):
        if vertex in visitedVerticies:
            continue
        if distance <= currentDistanceFromStart:
            currentVertex = vertex
            currentDistanceFromStart = distance
            
    return currentVertex, currentDistanceFromStart

def thereAreStillVerticiesToVisit(visitedVerticies, numberOfVerticies):
    return len(visitedVerticies) < numberOfVerticies
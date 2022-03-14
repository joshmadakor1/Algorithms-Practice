def dijkstrasAlgorithm(startIndex, edges):
    numberOfVerticies = len(edges)
    minDistanceFromStartToAllVerticies = [float('inf')] * numberOfVerticies
    minDistanceFromStartToAllVerticies[startIndex] = 0
    visitedVerticies = set()

    while thereAreStillVerticiesToVisit(numberOfVerticies, len(visitedVerticies)):
        currentVertexBeingVisited, distanceFromStartToCurrentVertexBeingVisited = getVertexWithMinDistanceFromStartThatHasntBeenVisitedYet(minDistanceFromStartToAllVerticies, visitedVerticies)
        if distanceFromStartToCurrentVertexBeingVisited == float('inf'):
            break # First time to discover unreachable node; algorithm finished
        visitedVerticies.add(currentVertexBeingVisited)

        for edge in edges[currentVertexBeingVisited]:
            currentVertexNeighbor, distanceFromCurrentVertexToCurrentVertexNeighbor = edge
            
            if currentVertexNeighbor is visitedVerticies:
                continue

            newDistanceFromStartToCurrentVertexNeighbor = distanceFromStartToCurrentVertexBeingVisited + distanceFromCurrentVertexToCurrentVertexNeighbor
            currentDistanceFromStartToCurrentVertexNeighbor = minDistanceFromStartToAllVerticies[currentVertexNeighbor]

            if newDistanceFromStartToCurrentVertexNeighbor < currentDistanceFromStartToCurrentVertexNeighbor:
                minDistanceFromStartToAllVerticies[currentVertexNeighbor] = newDistanceFromStartToCurrentVertexNeighbor

    return list(map(lambda x: -1 if x == float('inf') else x, minDistanceFromStartToAllVerticies))


def thereAreStillVerticiesToVisit(numberOfVerticies, numberOfVisitedVerticies):
    return numberOfVisitedVerticies < numberOfVerticies

def getVertexWithMinDistanceFromStartThatHasntBeenVisitedYet(minDistanceFromStartToAllVerticies, visitedVerticies):
    currentVertex = -1
    currentDistanceFromStart = float('inf')

    for vertex, distance in enumerate(minDistanceFromStartToAllVerticies):
        if vertex in visitedVerticies:
            continue
        if distance <= currentDistanceFromStart:
            currentVertex = vertex
            currentDistanceFromStart = distance

    return currentVertex, currentDistanceFromStart